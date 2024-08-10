import re

def validate_password(password):
  if len(password) < 8 or len(password) > 20:
    return False
  
  if not any(char.isdigit() for char in password):
    return False
  
  if not any(char.isupper() for char in password):
    return False
  
  if not any(char.islower() for char in password):
    return False
  
  if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/~`' for char in password):
    return False
  
  return True

def validate_password_with_error_messages(password):
  if len(password) < 8 or len(password) > 20:
    raise ValueError("Password length should be between 8 and 20 characters.")
  
  if not any(char.isdigit() for char in password):
    raise ValueError("Password should contain at least one digit.")
  
  if not any(char.isupper() for char in password):
    raise ValueError("Password should contain at least one uppercase letter.")
  
  if not any(char.islower() for char in password):
    raise ValueError("Password should contain at least one lowercase letter.")
  
  special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/~`'
  if not any(char in special_chars for char in password):
    raise ValueError(f"Password should contain at least one special character from the following: {special_chars}")
  
  return True

def validate_password_with_error_messages_regex(password):
  if not re.search(r'^.{8,20}$', password):
    raise ValueError("Password length should be between 8 and 20 characters.")
  
  if not re.search(r'\d', password):
    raise ValueError("Password should contain at least one digit.")
  
  if not re.search(r'[A-Z]', password):
    raise ValueError("Password should contain at least one uppercase letter.")
  
  if not re.search(r'[a-z]', password):
    raise ValueError("Password should contain at least one lowercase letter.")
  
  if not re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?/~`]', password):
    raise ValueError("Password should contain at least one special character.")
  
  return True
