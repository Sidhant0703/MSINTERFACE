import re

# ASCII Art Header
ascii_art = """
  ____   _    ____ ____         ____ _   _ _____ ____ _  _______ ____  
 |  _ \ / \  / ___/ ___|       / ___| | | | ____/ ___| |/ / ____|  _ \ 
 | |_) / _ \ \___ \___ \ _____| |   | |_| |  _|| |   | ' /|  _| | |_) |
 |  __/ ___ \ ___) |__) |_____| |___|  _  | |__| |___| . \| |___|  _ < 
 |_| /_/   \_\____/____/       \____|_| |_|_____\____|_|\_\_____|_| \_\
                                                                                         
                     Password Complexity Checker by Sidhanta Palei
"""

def check_password_complexity(password):
    # Define the criteria for complexity
    min_length = 8
    max_length = 20
    has_upper = re.compile(r'[A-Z]')
    has_lower = re.compile(r'[a-z]')
    has_digit = re.compile(r'[0-9]')
    has_special = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    common_passwords = set([
        'password', '123456', '123456789', 'qwerty', 'abc123', 'password1',
        '12345678', '12345', '1234567', 'welcome', 'letmein', 'password123'
    ])
    common_sequences = set([
        '123', 'abc', 'qwe', 'password', '111', '000'
    ])

    # Check length requirements
    if len(password) < min_length:
        return "Password must be at least 8 characters long."
    if len(password) > max_length:
        return "Password must be no more than 20 characters long."

    # Check for complexity
    if not has_upper.search(password):
        return "Password must contain at least one uppercase letter."
    if not has_lower.search(password):
        return "Password must contain at least one lowercase letter."
    if not has_digit.search(password):
        return "Password must contain at least one digit."
    if not has_special.search(password):
        return "Password must contain at least one special character."

    # Check for common passwords
    if password.lower() in common_passwords:
        return "Password is too common. Please choose a more unique password."

    # Check for common sequences
    if any(seq in password for seq in common_sequences):
        return "Password contains a common sequence. Please choose a more complex password."

    # If all checks pass
    return "Password is complex enough."

# Main program
if __name__ == "__main__":
    print(ascii_art)
    password = input("Enter the password to check: ")
    result = check_password_complexity(password)
    print(result)
