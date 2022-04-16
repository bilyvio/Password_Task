from string import (ascii_lowercase, ascii_uppercase, punctuation)


def has_character(password: str = "", part: str = "") -> bool:
    has_char = False

    for char in password:
        if char in part:
            has_char = True
            break

    return has_char


def is_valid(password: str = "") -> bool:
    try:
        if not password:
            return False

        val = True
        password = password.strip()
        digits = '0123456789'

        if (not has_character(password, ascii_lowercase)) \
                or (not has_character(password, ascii_uppercase)):
            print("- Password must contain both lowercase and uppercase characters")
            val = False

        if not has_character(password, digits):
            print("- Password must contain digits")
            val = False

        if not has_character(password, punctuation):
            print('- Password must contain one punctuation character (!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~')
            val = False

        if len(password) < 14:
            print("- Password must be at least 14 characters long")
            val = False

        if val:
            return val
    except:
        return False


def main():
    password = input("Enter your password: ")

    if is_valid(password):
        print("\nStrong password.")
    else:
        print("\nWeak password! Try again.")

