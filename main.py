import os
from turtle import delay
from delayPrint import delay_print, text_speed
from player import player


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    Exposition()
    Character_Creation()

def Menu():
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
    delay_print("Choose a class: ")
    print("B")
    delay_print("(input class to see more options ")





Menu()
