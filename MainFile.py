verion = "__V0.1.1__ Beta"

key = False
pants = False
knife = False
charhp = 10
enehp = 7

import random

def commands():
    print("########################################################")
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
        if key == False:
            if cabinetinput == "pick up knife":
                global knife
                knife = True
                print("You pick up the knife")
                kitchen()
        elif key == True:
            print("You already have this.")
            kitchen()
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
        if key == False:
            if pickup == "pick up key":
                global key
                key = True
                print("You take the key.")
                bedroom()
        elif key == True:
            if pickup == "pick up key":
                print("You already have this.")
                bedroom()
    if what == "inspect mirror":
        print("You have a nice shirt but your pants are torn and you could use some new one.")
    else:
        print("You can't do that.")
        bedroom()


def closet():
    print("-Broom closet-")
    print("There are many cobwebs in here, You find a broom, a dust pan, a locked box.")
    what1 = input("Enter a command: ")
    if what1 == "pick up box":
        box = True
        print("You pick up the box")
        closet()
    elif what1 == "exit":
        hallway()


def hallway():
    print("You are in a dim hallway, there are 4 doors here, one in each direction (north, south, east, and west).")
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
        sys.exit()
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
            if hitornot >= 3:
                print("THe old man punches you!")
                global charhp
                charhp = - 3
                print("You have recived 3 points of damage!")
                if charhp <= 0:
                    print("You died!")
                    sys.exit()
            else:
                print("The old man's punch misses you!")
            hitornot = random.randint(1, 5)
            if knife:
                print("You draw your knife and attack!")
                if hitornot >= 2:
                    print("You stab the attacker!")
                    enehp = - 6
            if knife == False:
                print("You raise you fists to prepare for a counter attack!")
                if hitornot >= 2:
                    print("You land a blow on your enemy!")
                    enehp = - 3
            if enehp <= 0:
                print("You won the battle!")
                print("Your enemy has died.")
                onedead = True
        def afterbattlebathroom():
            print("There is a dead body a toilet and a sink here")
            sinput = input("Enter a command: ")
            if sinput == "Inspect toilet":
                print("The toilet clean and white, and it still works. You lift the toilet bowl lid")
                print("to find a small rusty key laying at the bottom.")
                sinput = input("Take the key? y/n: ")
                if sinput == "y":
                    print("You take the rusty key.")
                    afterbattlebathroom()
                if sinput == "n":
                    print("You leave the key.")
                    afterbattlebathroom()
            elif sinput == "exit":
                hallway()
            elif sinput == "search body":
                print("You find a revolver, he must have been crazy not to use that in the battle.")
                print("You take the revolver thinking it might be useful.")
                global revolver
                revolver = True
                afterbattlebathroom()
            else:
                print("You cant do that")
                afterbattlebathroom()
        afterbattlebathroom()    


import sys

print("_________      ______    ______                  _________     _______                    ")
print("|  ____  \     |    |    |    |    _______       |  ____  \    | _____\     _______       ")
print("| |____|  \    |    |____|    |   /    ___\      | |____|  \   | |___| \   / ______\      ")
print("|         |    |     ____     |   |   |  ___     |         |   |       |   |  |  ___      ")
print("|   |\    /    |    |    |    |   |   |__| |     |   |\    /   |    ___/   |  |__| |      ")
print("|___| \__|     |____|    |____|   \________/     |___| \__|    |___|       \_______/      ")
print("                       ")
print("Welcome to RHGRPG Henry and Gabe's Text and Terminal Based RolePlaying Game!")
print("                      ")
start = input("Type start to start: ")

if start == "start":
    print("Ok lets begin.")
else:
    sys.exit()





print("Commands:")
print("Go <Direction> e.g.(west)")
print("quit")
print("pick up/drop <item>")
print("Also more specific commands e.g(open door)")
print("exit")
print("########################################################")
hallway()
