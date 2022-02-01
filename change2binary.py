"""
Implementing a function decimal_to_binary to convert a decimal number to a binary and vise versa with binary_to_decimal.
"""


def decimal_to_binary(num_dec: int):
    """
    Converts a decimal positive integer <num_dec> into a binary <num_bin>.

    :param num_dec: int
    :return num_bin: str
    """
    if num_dec == 0:
        return 0
    elif num_dec < 0:
        print("Don't you dare to give me a negative number! ;)")
        return -1
    num_bin = ""
    larger = 0
    while num_dec >= 2**larger:     # the = for a 2-pot e.g. 32. without it results in 11111 instead of 100000
        larger += 1
    smaller = larger - 1
    rest = num_dec
    ended = False
    for i in range(smaller, -1, -1):
        if ended:
            num_bin += "0"
            continue
        tmp = rest - 2**i
        if tmp < 0:
            num_bin += "0"
        elif tmp > 0:
            num_bin += "1"
            rest = tmp
        elif tmp == 0:
            num_bin += "1"
            ended = True
        i -= 1
    return num_bin


def binary_to_decimal(num_bin: str):
    """
    Converts a binary number <num_dec> into a decimal <num_bin>.

    :param num_bin: str
    :return num_dec: int
    """
    num_dec = 0
    for i, char in enumerate(reversed(num_bin)):
        if char == "0":
            pass
        elif char == "1":
            num_dec += pow(2, i)
        else:
            raise ValueError("Please only give me a string containing of 1 and 0!")
    return num_dec


if __name__ == '__main__':
    while True:
        menu = input("What would you want to convert?\nDecimal to binary (1)\nBinary to decimal (2)\nExit (3)")
        if menu in ["1", "2", "3"]:
            break
    if menu == "1":
        try:  # Try to convert to int.
            number_dec = int(input("Hey, which number should be converted from decimal to binary? "))
        except ValueError:  # If not possible, e.g. no number, raise error
            raise
        print(f"Converting {number_dec} into binary results in ", decimal_to_binary(number_dec))
    elif menu == "2":
        number_bin = input("Hey, which number should be converted from binary to decimal? ")
        print(binary_to_decimal(number_bin))
    elif menu == "3":
        exit()
