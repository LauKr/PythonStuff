import random as rnd


def get_char(char_set):
    char = char_set[rnd.randint(0, len(char_set))]
    return char


def generate_password(char_set, length=20):
    password = ''
    for i in range(length):
        password += get_char(char_set)
    return password


if __name__ == '__main__':
    password_length = input("Password length?")
    char_set = "abc"
    passwd = generate_password(char_set, length=8)
