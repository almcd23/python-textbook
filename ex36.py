from sys import exit

def final_room():
    print "You have won the game! You get to pet so many good dogs and cats."

def dog_room():
    print "You enter a room full of dogs."
    print "There are a lot of dogs in here."
    print "It is very loud."
    print "Are they good dogs?"

    choice = raw_input("> ")

    if "good" or "yes" in choice:
        final_room()
    elif "no" in choice:
        print "How dare you. They are good."
        dead()
    else:
        print "I don't understand. Try again!"

def cat_room():
    print "You enter a room full of cats."
    print "There are a lot of cats in here."
    print "How do you feel about so many cats?"

    choice = raw_input("> ")

    if "happy" or "good" in choice:
        dog_room()
    elif "not" in choice:
        print "Try again when you don't hate cats."
        start()
    else:
        start()

def math_room():
    print "You enter a room with equatioins on the wall."
    print "You're going to have to do some math."
    print "What is 2 x 5 - 3"

    choice = raw_input("> ")

    if choice == "7":
        final_room()
    else:
        dead("Sorry! Math is hard.")

def number_room():
    print "You enter a room with random numbers on the wall."
    print "Pick a number between 0 and 10."

    choice = raw_input("> ")

    if choice.isdigit():
        how_much = int(choice)
    else:
        print "I don't understand that. Try again"

    if how_much <= 5:
        print "Good job! You're going to advance."
        math_room()
    elif how_much > 5:
        print "Sorry. That's not what we're looking for."
        start()
    else:
        "I don't understand. Sorry."

def start():
    print "You start out in a small room."
    print "There are two doors."
    print "Which one do you choose?"

    choice = raw_input("Right or left?")

    if choice == "right":
        number_room()
    elif choice == "left":
        cat_room()
    else:
        print "I don't understand that. Try again"

def dead():
    print "Sorry, you have lost the game. Try again!"
    exit(0)

start()
