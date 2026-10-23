import os
from turtle import delay
from delayPrint import delay_print, text_speed
from player import player


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    Exposition()
    Character_Creation()
    ACT_1()

def Menu():
    clear()
    print("Point Neo")
    print("Play")
    print("Settings")
    print("quit")
    choice = input("Choose: ").lower()
    if choice == "play":
        main()
    elif choice == "settings":
        settings()
    else:
        print("choose a valid option")
        return


def settings():
    clear()
    print(f"text speed: {text_speed}")
    c = input("change text speed?: y/n").lower()
    if c == "y":
        p = input("enter new text speed: ")
    else:
        Menu()

def Exposition():
    clear()
    delay_print("3d printed meat has been getting cheaper...\n")
    delay_print("and healthcare costs keeps rising...\n")
    delay_print("so to those corpos it only made sense\n")
    input("press any button to continue...")
    clear()
    delay_print("They'd upload your brain to a centeral server, and print you a brand new body\n")
    delay_print("they always said it was some \"feat of human engineering\" \n")
    delay_print("but I always thought it was bullshit\n")
    input("press any button to continue...")
    clear()
    delay_print("the OGN corporation has had a chokehold on the western world\n")
    delay_print("Point Neos' govener hasn't done shit to slow it\n")
    delay_print("not to mention any foreign body - whos whole point is to fucking slow it\n")
    input("press any button to continue...")
    clear()

def Character_Creation():
    clear()
    player.char_name = input("Input Character name: ")
    while True:
        clear()
        delay_print("Choose a class: \n")
        print("Kernal")
        print("NetScaper")
        print("Slasher")
        class_input = input("input class name to see more options: ").lower()
        if class_input == "kernal":
            clear()
            delay_print("A Kernal is a combat specialist\n")
            delay_print("specilized in guns and CQB\n")
            i = input("choose Kernal? y/n: ").lower()
            if i == "y":
                player.char_class = "kernal"
                break
            else:
                pass
        elif class_input == "netscaper":
            clear()
            delay_print("A NetScaper specializes in hacking\n")
            delay_print("using any and all tech to their advantage\n")
            i = input("choose NetScaper? y/n: ").lower()
            if i == "y":
                player.char_class = "NetScaper"
                break
            else:
                pass
        elif class_input == "slasher":
            clear()
            delay_print("A slasher specializes in melee comabt\n")
            delay_print("adept in slashing weapons most of all\n")
            i = input("choose Slasher? y/n: ").lower()
            if i == "y":
                player.char_class = "Slasher"
                break
            else:
                pass

def ACT_1():
    clear()
    delay_print("some more exposition or something")









Menu()
