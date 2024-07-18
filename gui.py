import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from password_manager import PasswordManager
from translations import translations, current_language
from utils import get_password_strength

class PasswordManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title(translations[current_language]["title"])
        self.master.geometry("500x600")
        
        self.pm = PasswordManager()
        
        self.create_widgets()

    def create_widgets(self):
        # Language selection
        language_frame = ttk.Frame(self.master)
        language_frame.pack(fill=tk.X, padx=10, pady=5)
        ttk.Label(language_frame, text=translations[current_language]["language"] + ":").pack(side=tk.LEFT)
        self.language_var = tk.StringVar(value=current_language)
        language_menu = ttk.OptionMenu(language_frame, self.language_var, current_language, "en", "ja", "zh", command=self.change_language)
        language_menu.pack(side=tk.LEFT)

        # Master password
        self.master_password_label = ttk.Label(self.master, text=translations[current_language]["master_password"])
        self.master_password_label.pack(pady=5)
        self.master_password_entry = ttk.Entry(self.master, show="*")
        self.master_password_entry.pack(pady=5)
        self.master_password_button = ttk.Button(self.master, text="Set/Verify", command=self.set_verify_master_password)
        self.master_password_button.pack(pady=5)

        # Service
        self.service_label = ttk.Label(self.master, text=translations[current_language]["service"])
        self.service_label.pack(pady=5)
        self.service_entry = ttk.Entry(self.master)
        self.service_entry.pack(pady=5)

        # Username
        self.username_label = ttk.Label(self.master, text=translations[current_language]["username"])
        self.username_label.pack(pady=5)
        self.username_entry = ttk.Entry(self.master)
        self.username_entry.pack(pady=5)

        # Password
        self.password_label = ttk.Label(self.master, text=translations[current_language]["password"])
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(self.master, show="*")
        self.password_entry.pack(pady=5)

        # Password strength
        self.strength_label = ttk.Label(self.master, text=translations[current_language]["strength"])
        self.strength_label.pack(pady=5)
        self.strength_var = tk.StringVar()
        self.strength_display = ttk.Label(self.master, textvariable=self.strength_var)
        self.strength_display.pack(pady=5)

        # Buttons
        button_frame = ttk.Frame(self.master)
        button_frame.pack(pady=10)
        self.add_button = ttk.Button(button_frame, text=translations[current_language]["add"], command=self.add_password)
        self.add_button.grid(row=0, column=0, padx=5)
        self.get_button = ttk.Button(button_frame, text=translations[current_language]["get"], command=self.get_password)
        self.get_button.grid(row=0, column=1, padx=5)
        self.generate_button = ttk.Button(button_frame, text=translations[current_language]["generate"], command=self.generate_password)
        self.generate_button.grid(row=0, column=2, padx=5)
        self.edit_button = ttk.Button(button_frame, text=translations[current_language]["edit"], command=self.edit_password)
        self.edit_button.grid(row=1, column=0, padx=5, pady=5)
        self.delete_button = ttk.Button(button_frame, text=translations[current_language]["delete"], command=self.delete_password)
        self.delete_button.grid(row=1, column=1, padx=5, pady=5)
        self.list_button = ttk.Button(button_frame, text=translations[current_language]["list_all"], command=self.list_all_passwords)
        self.list_button.grid(row=1, column=2, padx=5, pady=5)

        # Export/Import buttons
        export_import_frame = ttk.Frame(self.master)
        export_import_frame.pack(pady=10)
        self.export_button = ttk.Button(export_import_frame, text=translations[current_language]["export"], command=self.export_data)
        self.export_button.grid(row=0, column=0, padx=5)
        self.import_button = ttk.Button(export_import_frame, text=translations[current_language]["import"], command=self.import_data)
        self.import_button.grid(row=0, column=1, padx=5)

        # Result
        self.result_label = ttk.Label(self.master, text=translations[current_language]["result"])
        self.result_label.pack(pady=5)
        self.result_text = tk.Text(self.master, height=10, width=50)
        self.result_text.pack(pady=5)

        # Bind password entry to strength check
        self.password_entry.bind('<KeyRelease>', self.check_password_strength)

    def change_language(self, lang):
        global current_language
        current_language = lang
        self.master.title(translations[current_language]["title"])
        self.master_password_label.config(text=translations[current_language]["master_password"])
        self.service_label.config(text=translations[current_language]["service"])
        self.username_label.config(text=translations[current_language]["username"])
        self.password_label.config(text=translations[current_language]["password"])
        self.strength_label.config(text=translations[current_language]["strength"])
        self.add_button.config(text=translations[current_language]["add"])
        self.get_button.config(text=translations[current_language]["get"])
        self.generate_button.config(text=translations[current_language]["generate"])
        self.edit_button.config(text=translations[current_language]["edit"])
        self.delete_button.config(text=translations[current_language]["delete"])
        self.list_button.config(text=translations[current_language]["list_all"])
        self.export_button.config(text=translations[current_language]["export"])
        self.import_button.config(text=translations[current_language]["import"])
        self.result_label.config(text=translations[current_language]["result"])

    def set_verify_master_password(self):
        password = self.master_password_entry.get()
        if self.pm.verify_master_password(password):
            messagebox.showinfo("Success", "Master password verified")
        else:
            self.pm.set_master_password(password)
            messagebox.showinfo("Success", "Master password set")

    def add_password(self):
        service = self.service_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.pm.add_password(service, username, password)
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, translations[current_language]["password_added"])

    def get_password(self):
        service = self.service_entry.get()
        result = self.pm.get_password(service)
        self.result_text.delete('1.0', tk.END)
        if result:
            username, password = result
            self.result_text.insert(tk.END, f"Username: {username}\nPassword: {password}")
        else:
            self.result_text.insert(tk.END, translations[current_language]["password_not_found"])

    def generate_password(self):
        password = self.pm.generate_password()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.check_password_strength(None)

    def edit_password(self):
        service = self.service_entry.get()
        username = self.username_entry.get()
        new_password = self.password_entry.get()
        self.pm.update_password(service, username, new_password)
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, translations[current_language]["password_updated"])

    def delete_password(self):
        service = self.service_entry.get()
        if messagebox.askyesno("Confirm", translations[current_language]["confirm_delete"]):
            self.pm.delete_password(service)
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert(tk.END, translations[current_language]["password_deleted"])

    def list_all_passwords(self):
        passwords = self.pm.list_all_passwords()
        self.result_text.delete('1.0', tk.END)
        for service, username, password in passwords:
            self.result_text.insert(tk.END, f"Service: {service}\nUsername: {username}\nPassword: {password}\n\n")

    def export_data(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json")
        if filename:
            self.pm.export_data(filename)
            messagebox.showinfo("Success", translations[current_language]["export_success"])

    def import_data(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            self.pm.import_data(filename)
            messagebox.showinfo("Success", translations[current_language]["import_success"])

    def check_password_strength(self, event):
        password = self.password_entry.get()
        strength = get_password_strength(password)
        if strength == "weak":
            self.strength_var.set(translations[current_language]["weak"])
            self.strength_display.config(foreground="red")
        elif strength == "medium":
            self.strength_var.set(translations[current_language]["medium"])
            self.strength_display.config(foreground="orange")
        else:
            self.strength_var.set(translations[current_language]["strong"])
            self.strength_display.config(foreground="green")