import random
import os
import time

def clear():
    os.system("cls")

def print_hangman(arg):
    print()
    print("\t\t +-------+-+")
    print("\t\t |       | |")
    print("\t\t {}       | |".format(arg[0]))
    print("\t\t{}{}{}      | |".format(arg[2], arg[1], arg[3]))
    print("\t\t {}       | |".format(arg[4]))
    print("\t\t{} {}      | |".format(arg[5],arg[6]))
    print("\t\t         | |")
    print("\t  _______________|_|___")
    print("\t  `````````````````````")
    print()

def print_hangman_win():
    print()
    print("\t\t +-------+-+")
    print("\t\t |       | |")
    print("\t\t         | |")
    print("\t\t         | |")
    print("\t\t O       | |")
    print("\t\t/|\\      | |")
    print("\t\t |       | |")
    print("\t  ______/_\\______|_|___")
    print("\t  ``````````````````````")
    print()

def print_word(arg):
    print()
    print("\tGUESSE THE WORD : ", end="")
    for i in arg:
        print(i, end="")
    print()
    print() 

def check_win(arg):
    for char in arg:
        if char == '_':
            return False
    return True    
 
def hangman_game(word):
    clear()

    word_display = []

    correct_letters = []
 
    incorrect = []
 
    chances = 0

    hangman_values = ['O','|','/','\\','|','/','\\']

    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

    for char in word:
        if char.isalpha():
            word_display.append('_')
            correct_letters.append(char.upper())
        else:
            word_display.append(char)

    while True:
        print("hANGMAN GAME !!")
        print()
        print("\tIncorrect Guesses : ", incorrect)
        print()
        print_hangman(show_hangman_values)
        print_word(word_display)            
        
 
        ch = input("\tMake a Guess   : ")
        if len(ch) != 1:
            clear()
            print("\tWrong Choice!! Try Again")
            time.sleep(2)
            clear()
            continue
        if not ch.isalpha():
            clear()
            print("\tInvalid Guess!! Try Again")
            time.sleep(2)
            clear()
            continue
        if ch.upper() in incorrect or ch.upper() in word_display:
            clear()
            print("\tAlready Tried!!")
            time.sleep(2)
            clear()
            continue   
        if ch.upper() not in correct_letters:
            incorrect.append(ch.upper())
            show_hangman_values[chances] = hangman_values[chances]
            chances = chances + 1
            if chances == len(hangman_values):
                clear()
                print("hANGMAN GAME !!")
                print('''
                GAME OVER!!!

                YOU LOSE !!
                ''')
                time.sleep(1)
                print_hangman(hangman_values)
                print("\tThe word is :", word.upper())
                break
        else:
            for i in range(len(word)):
                if word[i].upper() == ch.upper():
                    word_display[i] = ch.upper()

            if check_win(word_display):
                clear()
                print("hANGMAN GAME !!")
                print('''
                CONGRATULATTIONS!!!

                    YOU WIN !!
                ''')                
                time.sleep(1)
                print_hangman_win()
                print("\tThe Word is :", word.upper())
                break
        clear() 


topics = {1: "DC characters", 2:"Marvel characters", 3:"Anime characters", 4:"Fruits"}
 
dataset = {"DC characters":["SUPERMAN", "JOKER", "HARLEY QUINN", "GREEN LANTERN", "FLASH", "WONDER WOMAN", "AQUAMAN", "BATMAN"],
             "Marvel characters":["CAPTAIN AMERICA", "IRON MAN", "THANOS", "HAWKEYE", "BLACK PANTHER", "BLACK WIDOW"],
             "Anime characters":["MONKEY D. LUFFY", "RORONOA ZORO", "LIGHT YAGAMI", "MIDORIYA IZUKU", "NARUTO UZUMAKI"],
             "Fruits":["Dragon Fruit", "Apple", "Kiwi", "Mango", "Banana", "Pineapple", "Cherry"]
             }
     
print("hANGMAN GAME !!")
while True:

    time.sleep(0.5)
    print()
    print("\t-----------------------------------------")
    print("\t\t\tGAME MENU")
    print("\t-----------------------------------------")
    for key in topics:
        print("\tPress", key, "to select", topics[key])
    print("\tPress", len(topics)+1, "to quit")    
    print()
    time.sleep(1)
    try:
        choice = int(input("\tEnter your choice = "))
    except ValueError:
        clear()
        print("\tWrong choice!!! Try again")
        time.sleep(1.5)
        clear()
        print("hANGMAN GAME !!")
        continue

    if choice > len(topics)+1:
        clear()
        print("\tNo such topic!!! Try again.")
        time.sleep(1.5)
        clear()
        print("hANGMAN GAME !!")
        continue   
 
    elif choice == len(topics)+1:
        clear()
        print("\tThank You for Playing!")
        time.sleep(3)
        break
 
    chosen_topic = topics[choice]
    game_word = random.choice(dataset[chosen_topic])
    hangman_game(game_word)