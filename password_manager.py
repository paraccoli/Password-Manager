import sqlite3
import hashlib
import secrets
import string
from cryptography.fernet import Fernet
import base64
import json

class PasswordManager:
    def __init__(self):
        self.conn = sqlite3.connect('passwords.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS passwords
                          (id INTEGER PRIMARY KEY, service TEXT, username TEXT, password TEXT)''')
        self.key = None
        self.fernet = None

    def set_master_password(self, password):
        salt = secrets.token_bytes(16)
        key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        self.key = key
        self.fernet = Fernet(base64.urlsafe_b64encode(key))
        
        with open('salt.bin', 'wb') as f:
            f.write(salt)

    def verify_master_password(self, password):
        try:
            with open('salt.bin', 'rb') as f:
                salt = f.read()
            key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
            self.key = key
            self.fernet = Fernet(base64.urlsafe_b64encode(key))
            return True
        except:
            return False

    def add_password(self, service, username, password):
        encrypted_password = self.fernet.encrypt(password.encode()).decode()
        self.c.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
                       (service, username, encrypted_password))
        self.conn.commit()

    def get_password(self, service):
        self.c.execute("SELECT username, password FROM passwords WHERE service=?", (service,))
        result = self.c.fetchone()
        if result:
            username, encrypted_password = result
            decrypted_password = self.fernet.decrypt(encrypted_password.encode()).decode()
            return username, decrypted_password
        return None

    def update_password(self, service, username, new_password):
        encrypted_password = self.fernet.encrypt(new_password.encode()).decode()
        self.c.execute("UPDATE passwords SET username=?, password=? WHERE service=?",
                       (username, encrypted_password, service))
        self.conn.commit()

    def delete_password(self, service):
        self.c.execute("DELETE FROM passwords WHERE service=?", (service,))
        self.conn.commit()

    def list_all_passwords(self):
        self.c.execute("SELECT service, username, password FROM passwords")
        results = self.c.fetchall()
        decrypted_results = []
        for service, username, encrypted_password in results:
            decrypted_password = self.fernet.decrypt(encrypted_password.encode()).decode()
            decrypted_results.append((service, username, decrypted_password))
        return decrypted_results

    def generate_password(self, length=16):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def export_data(self, filename):
        data = self.list_all_passwords()
        with open(filename, 'w') as f:
            json.dump(data, f)

    def import_data(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        for service, username, password in data:
            self.add_password(service, username, password)

    def close(self):
        self.conn.close()
