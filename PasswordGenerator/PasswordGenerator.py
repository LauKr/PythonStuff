import random as rnd
from PyQt5 import QtWidgets, uic
import sys
import pyperclip


def get_char_set(selection="all"):
    if selection == "numbers":
        char_set = "1234567890"
    elif selection == "alpha":
        char_set = "abcdefghijklmnopqrstuvwxyz"
    elif selection == "Alpha":
        char_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif selection == "all":
        char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return char_set


def get_char(char_set):
    char = char_set[rnd.randint(0, len(char_set) - 1)]
    return char


def generate_password(char_set, length=20):
    password = ''
    for i in range(length):
        password += get_char(char_set)
    return password


def main(pass_length=20, characters="all"):
    # char_set = get_char_set(characters)
    password = generate_password(characters, length=pass_length)
    return password


def initialize_password_generation():
    def copy_passwd():
        pyperclip.copy(window.textBrowser.toPlainText())
        return 0

    def run():
        password_length = window.spinBox_passwd_length.value()
        character_list = ""
        if window.checkBox_numbers.isChecked():
            character_list += "1234567890"
        if window.checkBox_alpha.isChecked():
            character_list += "abcdefghijklmnopqrstuvwxyz"
        if window.checkBox_ALPHA.isChecked():
            character_list += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if window.checkBox_basic_symbols.isChecked():
            character_list += "!"
        if window.checkBox_extended_symbols.isChecked():
            character_list += "#"
        if window.checkBox_ticks.isChecked():
            character_list += "'"
        if not (window.checkBox_numbers.isChecked() or window.checkBox_alpha.isChecked() or
                window.checkBox_ALPHA.isChecked() or window.checkBox_basic_symbols.isChecked() or
                window.checkBox_extended_symbols.isChecked() or window.checkBox_ticks.isChecked()):
            window.label.setStyleSheet("background-color: lightgreen")
            return 1
        password = main(pass_length=password_length, characters=character_list)
        window.textBrowser.setText(password)
        return 0
    app = QtWidgets.QApplication(sys.argv)
    window = uic.loadUi("PasswordGeneratorGUI.ui")
    # Signals
    window.pushButton_exit.clicked.connect(sys.exit)
    window.pushButton_copy.clicked.connect(copy_passwd)
    window.generate_password.clicked.connect(run)
    # Actions
    #
    window.show()
    app.exec()


if __name__ == "__main__":
    #    password_length = int(input("Password length?"))
    #    passwd = main(password_length, "all")
    #    print("Your generated password is ", passwd)
    initialize_password_generation()