#__V0.3__

key = False
pants = False
knife = False
charhp = 10

import random

def commands():
    print("Commands:")
    print("Go <Direction> e.g.(west)")
    print("quit")
    print("pick up/drop <item>")
    print("Also more specific commands e.g(open door)")
    print("exit")
    print("########################################################")


def kitchen():
    print("-Kitchen-")
    print("You walk into a room that smells of onions. You assume it is the kitchen because of the pots and pans.")
    print("There is a counter and a table and several cabinets.")
    kitcheninput = input("Enter a command: ")
    if kitcheninput == "exit":
        hallway()
    if kitcheninput == "inspect cabinets":
        print("The cabinets are empty except for a rusty knife.")
        cabinetinput = input("Enter a command:")
        if cabinetinput == "pick up knife":
            global knife
            knife = True
            print("You pick up the knife")
        if cabinetinput == "exit":
            kitchen()
    else:
        print("You cant do that.")
        bedroom()


def bedroom():
    print("-Bedroom-")
    print("You walk into a musty room with a dusty bed against the wall.")
    print("On the opposite side of the room the is a dresser with a large mirror and a flickering lamp atop it.")
    what = input("Enter a command: ")
    if what == "exit":
        hallway()
    if what == "inspect dresser":
        print("You rummage through the dresser only to find pants and a copper key.")
        pickup = input("enter a command: ")
        if pickup == "pick up key":
            global key
            key = True
            print("You take the key.")
        bedroom()
    if what == "inspect mirror":
        print("You have a nice tank top but your pants are torn and you could use some new.")
    else:
        print("You can't do that.")
        bedroom()
e

def closet():
    print("-Broom closet-")
    print("There are many cobwebs in here, You find a broom, a dust pan, a locked box.")


def hallway():
    print("You are in a dim hallway, there are 4 doors here, one in each direction(north, south, east, and west)")
    hall = input("enter a command: ")
    if hall == "go north":
        bathroom()
    elif hall == "go west":
        kitchen()
    elif hall == "go east":
        bedroom()
    elif hall == "go south":
        print("You exit the hallway.Into a dark room you trip and fall on a spike.")
        print("#######################")
        print("#YOU DIE!!!!!!!!!!!!!!#")
        print("#######################")
        sys.exit
    elif hall == "help":
        commands()
        hallway()
    else:
        print("You can't do that")
        hallway()


def bathroom():
    if key == False:
        print("This door is locked")
    elif key == True:
        print("You turn the key in the lock. It makes a satisfying click. You open the door to find a crazed old man")
        print("crouched on the floor. He springs up and attacks you!")
        onedead = False
        while onedead == False:
            hitornot = random.randint(1, 5)
            if hitornot > 3:
                print("THe old man punches you!")
                global charhp
                charhp = - 3
                print("You have recived 3 points of damage!")
                if charhp <= 0:
                    print("You died!")
                    onedead = True
            else:
                print("The old man's punch misses you!")
            hitornot = random.randint(1, 5)
            if knife:
                print("You draw your knife and attack!")
                if hitornot >= 2:
                    print("You stab the attacker!")



import sys

print("______    ______                  _________         _______                  ")
print("|    |    |    |    _______       |  ____  \        | _____\     ______        ")
print("|    |____|    |   /    ___\      | |____|  \       | |___| \   / _____\      ")
print("|    |__  |    |  |    |  ___     |         |       |       |  |  |  __      ")
print("|    |    |    |  |    |__| |     |   |\    /       |    ___/  |  |__| |      ")
print("|____|    |____|   \________/     |___| \__|        |___|       \______/         ")
print("                       ")
print("Welcome to HGRPG Henry and Gabe's RolePlaying Game!")
print("                      ")
start = input("Type start to start")

if start == "start":
    print("Ok lets play")
else:
    sys.exit





print("Commands:")
print("Go <Direction> e.g.(west)")
print("quit")
print("pick up/drop <item>")
print("Also more specific commands e.g(open door)")
print("exit")
print("########################################################")
hallway()
