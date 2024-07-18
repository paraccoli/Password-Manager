import re

def get_password_strength(password):
    if len(password) < 8:
        return "weak"
    elif len(password) < 12:
        return "medium"
    elif re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$', password):
        return "strong"
    else:
        return "medium"
