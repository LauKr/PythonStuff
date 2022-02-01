import numpy as np


def lottery(mode='rand', number_guesses=6):
    welcome()
    if mode == 'rand':
        while True:
            win_numbers = np.random.randint(1, 50, number_guesses)
            # print(win_numbers)
            if win_numbers.size == np.unique(win_numbers).size:
                break
    elif mode == 'test':
        print("!--- Test mode ---!")
        insert_wins = False
        if insert_wins:
            win_numbers = get_guess(number_guesses)
        else:  # If not 6 picks this has to be modified
            win_numbers = np.array([4, 6, 45, 1, 26, 41])
    else:
        raise ValueError("<mode> has to be either 'rand' or 'test'. Passed through lottery(mode).")
    guess = get_guess(number_guesses)
    corrects = check_corrects(guess, win_numbers)
    print(f"correct numbers: {win_numbers}")
    if corrects == number_guesses:  # All correct
        you_won()
    elif corrects == 0:  # All wrong
        you_lost()
    else:
        you_lost()
    return 0


def get_guess(number_guesses=6):
    print(f'You can pick {number_guesses} integer numbers between 1 and 49\n')
    while True:
        guesses = np.empty(number_guesses)
        for i in range(number_guesses):
            inserted_value = input(f'What is your number No. {i+1}? ')
            try:
                guesses[i] = inserted_value
            except ValueError as verr:  # s does not contain anything convertible
                print("Your inserted number seems to be not a number? o.O \n\n", verr)
                print("Please reconsider using real numbers ;)")
                raise
            except Exception as ex:
                print("Your inserted number seems to be not a number? o.O \n\n", ex)
                print("Please reconsider using real numbers ;)\nOtherwise more exceptions will rise")
                raise
        are_all_int = [i.is_integer() for i in guesses]
        for is_it_int in are_all_int:
            if not is_it_int:
                print(f'All inserted numbers should be integers!\n'
                      'Please only use whole numbers between 1 and 49. E.g. 4, not 4.0')
        else:
            if int(max(guesses)) >= 50 or int(min(guesses)) < 1:
                print("Please only use integer numbers between 1 and 49 (included).")
            else:
                if guesses.size != np.unique(guesses).size:
                    print("Please don't use one number twice or you'll loose by design.")
                else:
                    break
        print("\nLet's try again!\n")
    print(f"Your guesses: {guesses}")
    return guesses


def check_corrects(guesses, wins):
    num_corrects = 0
    for i, guess in enumerate(guesses):
        if guess in wins:
            num_corrects += 1
    return num_corrects


def you_lost(kids_mode=True):
    kids_mode = True
    if kids_mode:
        lost_text = """
                        ───▄▄▄
                        ─▄▀░▄░▀▄
                        ─█░█▄▀░█
                        ─█░▀▄▄▀█▄█▄▀
                        ▄▄█▄▄▄▄███▀"""
    else:
        lost_text = """
░░░░░░░░░░░█▀▀░░█░░░░░░
░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░
░░░░░░█░█░░░░░░░░░░▐░░░
░░░░░░▐▐░░░░░░░░░▄░▐░░░
░░░░░░█░░░░░░░░▄▀▀░▐░░░
░░░░▄▀░░░░░░░░▐░▄▄▀░░░░
░░▄▀░░░▐░░░░░█▄▀░▐░░░░░
░░█░░░▐░░░░░░░░▄░█░░░░░
░░░█▄░░▀▄░░░░▄▀▐░█░░░░░
░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░
░░▐█▐▄░░▀░░░░░░▐░█▄▄░░░
░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░
░░░░░░░░░░░░░░░░░░░░░░░"""
    print("You Lost\n\n", lost_text, "\n\nYou Lost")
    return 0


def you_won():
    won_text = """
                                                              ██████▒▒██                    
                    ██████                              ████████▒▒▒▒██                  
                  ██░░░░░░████████████          ████████████████▒▒▒▒██                  
                  ██░░░░░░████▒▒▒▒▒▒▒▒██████████▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒██                  
                ██░░▒▒░░░░████▒▒▒▒████▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒████▒▒██                  
                ██░░░░▒▒██████▒▒██████████▒▒▒▒░░▒▒▒▒░░░░░░▒▒░░░░██████                  
              ██░░░░░░▒▒██████▒▒░░░░██████▒▒▒▒░░░░▒▒▒▒░░░░▒▒░░░░░░████                  
              ██▒▒▒▒▒▒██    ████░░░░░░██████▒▒░░░░░░▒▒░░░░░░░░░░░░████                  
              ██░░▒▒▒▒██    ████░░░░░░░░████░░░░░░░░░░░░░░░░░░░░██████                  
              ██▒▒░░░░██      ████░░░░░░██████░░░░░░░░░░░░░░░░████████                  
              ██▒▒▒▒▒▒██      ██████░░████████░░░░░░░░░░░░░░░░████░░██                  
              ██▒▒▒▒▒▒██        ████████░░░░░░██████░░░░░░░░░░  ██  ██                  
              ██▒▒░░░░░░██      ██▒▒▒▒▒▒░░░░██████████░░    ░░████  ██████              
              ██░░░░▒▒▒▒▒▒████████▒▒▒▒░░░░░░██░░██████░░      ▒▒▒▒    ░░                
                ██▒▒▒▒▒▒████▒▒░░██░░░░░░░░  ░░    ████░░          ████████              
                ██▒▒▒▒██▒▒▒▒░░░░██▒▒▒▒▒▒░░      ██████    ░░░░      ██                  
                  ████▒▒▒▒░░░░▒▒▒▒▒▒░░░░▒▒▒▒░░  ████      ████    ████                  
                  ██░░▒▒░░░░▒▒▒▒░░░░░░░░                        ████                    
                ██▒▒░░░░░░░░▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒              ████                      
                ██▒▒░░░░░░░░▒▒░░░░░░▒▒░░░░░░░░            ██████                        
                ██▒▒▒▒░░░░░░▒▒░░░░░░▒▒░░▒▒▒▒░░░░░░░░░░░░▒▒▒▒██                          
                ██▒▒▒▒░░░░░░▒▒░░░░░░░░░░▒▒▒▒▒▒░░░░  ░░▒▒▒▒▒▒░░██                        
              ██▒▒▒▒▒▒▒▒░░░░      ░░░░░░░░▒▒▒▒██    ██░░░░░░░░██                        
              ██▒▒▒▒░░░░░░░░        ░░░░░░░░░░██  ░░██        ░░██                      
              ██  ░░░░░░░░░░  ░░██████  ░░  ░░████████          ██                      
              ██        ░░██████      ██        ██    ██    ░░  ██                      
              ██        ████████      ██░░        ██  ██░░░░    ██                      
              ██      ██                ██  ░░░░  ██    ████████                        
                ██████                  ██░░▒▒  ██                                      
"""
    print("You won")
    print(won_text)
    print('\n\nCongratulations. You won!')
    return 0


def welcome():
    welcome_text = """
    
███████████████████████████████████████████████████████████████████████
█▄─▄████▀▄─██▄─██─▄█░█─▄▄▄▄███▄─▄███─▄▄─█─▄─▄─█─▄─▄─█▄─▄▄─█▄─▄▄▀█▄─█─▄█
██─██▀██─▀─███─██─██▄█▄▄▄▄─████─██▀█─██─███─█████─████─▄█▀██─▄─▄██▄─▄██
▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▄▀▀▀▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀


                    ┌────────── •✧✧• ──────────┐
                     - Welcome to the lottery!- 
                    └────────── •✧✧• ──────────┘"""
    print(welcome_text)
    return 0


if __name__ == '__main__':
    lottery(mode='rand')
