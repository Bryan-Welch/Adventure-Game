import time
import random

enemy = random.choice(['Troll', 'Dragon', 'Ogre'])
items = []


def print_pause(message, pause=1):
    print(message)
    time.sleep(pause)


def intro(enemy):
    print_pause("You find yourself standing in an open field, filled with \n"
                "grass and yellow wildflowers. Rumor has it that a wicked \n"
                + enemy + " is somewhere around here, and has been \n"
                "terrorizing the nearby village. \n", 3)

    print_pause("Enter 1 to knock on the door of the house. \n"
                "Enter 2 to peer into the cave. \n"
                "What would you like to do? \n")

    choice = input("(Please enter 1 or 2)\n")
    if choice == '1':
        house(items, enemy)
    elif choice == '2':
        cave(items, enemy)
    else:
        print_pause("(Please choose 1 or 2)\n")
        intro(enemy)


def house(items, enemy):
    print_pause("You approach the house and knock on the door, the door \n"
                "creaks open slowly and you cautiously enter. As you \n"
                "cross the doors threshhold you feel the presence of \n"
                "something, something not human. Suddenly a \n"
                + enemy + " appears from the other room, as soon as it \n"
                "spots you it charges you in a fit of rage. Will you \n"
                "stand and fight with your trusty dagger or retreat and \n"
                "attempt to find a new path to defeat your foe? \n", 3)
    choice = input("(Please enter 1 to fight or 2 to retreat)\n")
    if choice == '1':
        fight(items, enemy)
    elif choice == '2':
        field(items, enemy)
    else:
        print_pause("(Please choose 1 or 2)\n")
        house(items, enemy)


def cave(items, enemy):
    if 'sword' in items:
        print_pause("You step into the cave again, it seems to be empty. \n"
                    "You turn around and return to the field \n")
        field(items, enemy)
    else:
        print_pause("You peer into the cave. \n"
                    "As you do you notice a glint of light in the back. \n"
                    "You approach the light and as you get closer an object \n"
                    "takes shape and appears out of a mystterious swirling \n"
                    "mist. The sword of Asgoloth appears, a legendary \n"
                    "weapon that was thought lost at the battle of Wraiths \n"
                    "Veil. You pick up the sword and you can feels its \n"
                    "power flowing through you, no beast can stand against \n"
                    "you now, and you know it. \n", 3)

        items.append("sword")
    field(items, enemy)


def field(items, enemy):
    if 'sword' in items:
        print_pause("With Asgoloth in hand you feel confident about your "
                    "victory, now to find the beast. \n")

    else:
        print_pause("You return to the field. \n"
                    "Something draws you toward the cave, it feels as though "
                    "something is calling to you \n")
    choice = input("Where would you like to go? \n"
                   "Press 1 for cave press 2 for house \n")
    if choice == '1':
        cave(items, enemy)
    elif choice == '2':
        house(items, enemy)
    else:
        print_pause("I don't recognize that answer please choose 1 for cave "
                    "or 2 for house \n")
        field(items, enemy)


def fight(items, enemy):
    if 'sword' in items:
        print_pause("The " + enemy + " charges but you stand your ground, \n"
                    "Asgoloth in hand. As the " + enemy + " is about to \n"
                    "attack you slide out of the way with exceptional \n"
                    "timing and reflexes. The " + enemy + " now in the \n"
                    "middle of its attack and off balance is not prepared \n"
                    "for what's to come. You swing Asgoloth with all your \n"
                    "might and it bites into flesh, the " + enemy + " \n"
                    "screams out in pain as it's life force is drained by \n"
                    "Asgoloth's sting. After a moment of struggle \n"
                    "the " + enemy + " drops to the ground, defeated. You "
                    "are victorious!", 3)
    else:
        print_pause("The " + enemy + "charges but you stand your ground, \n"
                    "your dagger will be more than enough to handle this \n"
                    "beast. As the " + enemy + " is about to attack you \n"
                    "slide out of the way, the " + enemy + " is not fooled \n"
                    "and in quicker than it appears. You swipe at it with \n"
                    "your dagger but just nick it's skin, not enough to \n"
                    "injure it greatly but enough to anger it. \n"
                    "The" + enemy + " grabs your feet as you are unbalanced \n"
                    "from your failed counter attack, he lifts you in the \n"
                    "air and slams you into the hard ground. Your vision \n"
                    "goes black as you stare at the ceinling of the house, \n"
                    "your last sight is of the " + enemy + " standing over \n"
                    "you, a smile on its face. You are defeated.\n", 3)
        play_again()


def play_again():
    choice = input("Would you like to play again y/n?")
    if choice == 'y':
        play_game(items, enemy)
    elif choice == 'n':
        print_pause("Thank you for playing!")
    else:
        print_pause("I didn't recongnize your answer please choose y/n.")
        play_again()


def play_game(items, enemy):
    intro(enemy)


play_game(items, enemy)
