import random
import array
import string
from task1 import is_valid

length = random.randint(14, 40)
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
punctuation_characters = list(string.punctuation)
password_comb = digits + uppercase_letters + lowercase_letters + punctuation_characters


def create_password():

    global pass_temp_list
    rand_digit = random.choice(digits)
    rand_upper = random.choice(uppercase_letters)
    rand_lower = random.choice(lowercase_letters)
    rand_punct = random.choice(punctuation_characters)

    pass_temp = rand_digit + rand_upper + rand_lower + rand_punct

    for x in range(length - 4):
        pass_temp = pass_temp + random.choice(password_comb)
        pass_temp_list = array.array('u', pass_temp)
        random.shuffle(pass_temp_list)

    password = ""
    for x in pass_temp_list:
        password = password + x

    return password


password_created = create_password()
print(create_password())
print(is_valid(password_created))
