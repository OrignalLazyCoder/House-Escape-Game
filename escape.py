from time import *
from random import *
import os, sys

global health
global gold


def check():
    if (health <= 0):
        kill()
    if (gold > 50):
        win()


def bye():
    global health
    global gold
    print("\n\n\nOrignal Idea by: Arpit Sharma")
    print("Coder: Arpit Sharma")
    print("Support LazyCoder!")
    f=open("score.txt",'r')
    print("Last score was "+f.read())
    f.close()
    f=open("score.txt",'w')
    f.write("gold:"+str(gold)+" Health:"+str(health))
    f.close()
    i = input()
    sys.exit()


# if health is less than 0 then we die
def kill():
    print("Game over. Ghost killed you.")
    bye()


# if gold>50 we win the game
def win():
    print("YEAH! I AM FREE TO GO.")
    print("GHOST: ARHHHHH!")
    sleep(1)
    print("\nYOU WIN!!!")
    bye()


def display():
    global health
    global gold
    print("You have " + str(gold) + " gold coins And " + str(health) + " health Left")
    sleep(3)
    print("\n\n")


def wrong():
    global health
    global gold
    print("Enter valid choice")
    health = health - (0.15 * health)
    print("Ghost took your health away")
    display()
    sleep(2)


# function to start the game
def start():
    print("welcome")
    print("This game is based on random events. You are trapped in a house with ghosts and wild animals. You need to search the house to collect sufficient ammount of coins to exit the house OR DIE!")
    global gold
    global health
    health = 50
    gold = 0
    lobby()


# function for getting command
def promptgate():
    print("Enter the direction you want to go:(n/s/e)")
    command = str(input())
    return command


# funtion for lobby
def lobby():
    global gold
    global health
    print("You are in lobby Right now!")
    print("There are 4 gates in front of you.You need to find gold to get out of this Haunted house.Be safe.There are ghosts in this house!")
    print("\nGo north to see bedroom")
    print("Go south to see garden")
    print("Go east to see bathroom")
    command = promptgate()
    if (command == "n"):
        bedroom()
    elif (command == "s"):
        garden()
    elif (command == "e"):
        bathroom()
    else:
        print("Enter valid direction")
        n = randint(1, 10)
        if (n % 2 == 0):
            health = health - 5
            print("You entered the wrong choice.A wild Ghost took your health")
            print("You health is " + str(health))
        else:
            print("Time is less.A ghost just passed near from you")
        sleep(2)
        lobby()


# funtions in bedroom are controlled from here
def bedroom():
    global gold
    global health
    check()
    display()
    print("You are in bedroom right now. There is a bed,Almirah and window.")
    sleep(1)
    print("Enter your choice.\nb=bed\na=Almirah\nw=Window \nq=Go back to lobby:")
    choice = str(input())
    if (choice == "b"):
        bed()
    elif (choice == "a"):
        almirah()
    elif (choice == "w"):
        window()
    elif (choice == "q"):
        lobby()
    else:
        print("Enter valid direction")
        n = randint(1, 10)
        if (n % 2 == 0):
            health = health - 5
            print("You entered the wrong choice.A wild Ghost took your health")
            print("You health is " + str(health))
        else:
            print("Time is less.A ghost just passed near from you")
        sleep(2)
        print("YOU WERE THROWN BACK TO LOBBY")
        lobby()


def bedchoice():
    global health
    global gold
    sleep(1)
    print("There is a \np=pillow\nm=mattress\nb=Bedsheet\nc=cloths\nq=Back to lobby.What you want to search?")
    choice = str(input())
    display()
    return choice


def bed():
    check()
    global health
    global gold
    choice = bedchoice()
    display()
    if (choice == "p"):
        n = randint(1, 10)
        if (n % 3 == 0):
            gold = gold + n;
            print("You found " + str(n) + " in this pillow")
            display()
            sleep(1)
        else:
            print("You found nothing. Come back later. Ghosts keep changing the location of gold in this house")
            print("GHOST: YOU WASTED YOUR TIME COMING HERE.YOU CANNOT RUN!!!")
            health = health - n
            display()
        bed()
    elif (choice == "m"):
        n = randint(1, 8)
        if (n % 4 == 0):
            gold = gold + n;
            print("You found " + str(n) + " in this Matress")
            display()
            sleep(1)
        else:
            print("You found nothing. Come back later. Ghosts keep changing the location of gold in this house")
            print("GHOST: YOU WASTED YOUR TIME COMING HERE.YOU CANNOT RUN!!!")
            health = health - n
            display()
        bed()
    elif (choice == "b"):
        n = randint(1, 10)
        if (n % 3 == 0):
            gold = gold + n;
            print("You found " + str(n) + " in bedsheet")
            display()
            sleep(1)
        else:
            print("You found nothing. Come back later. Ghosts keep changing the location of gold in this house")
            print("GHOST: YOU WASTED YOUR TIME COMING HERE.YOU CANNOT RUN!!!")
            health = health - n
            display()
        bed()
    elif (choice == "c"):
        n = randint(1, 5)
        if (n % 2 == 0):
            gold = gold + n;
            print("You found " + str(n) + " in these old clothes")
            display()
            sleep(1)
        else:
            print("You found nothing. Come back later. Ghosts keep changing the location of gold in this house")
            print("GHOST: YOU WASTED YOUR TIME COMING HERE.YOU CANNOT RUN!!!")
            health = health - n
            display()
        bed()
    elif (choice == "q"):
        print("GHOST:YOU ARE TOO AFRAID TO SEARCH HERE")
        bedroom()
    else:
        wrong()
        bed()


def almirahchoice():
    print(
        "Oh! I see a big almirah here.\nThere are two columns in this almirah \n1.Big \n2. Small \n3.Go Back. Enter you choice:(1/2)")
    choice = (input())
    display()
    return choice


def almirah():
    global health
    global gold
    check()
    choice = almirahchoice()
    if (choice == "1"):
        n = randint(5, 9)
        if (n % 2 == 0):
            gold = gold + n
            print("You found " + str(gold) + " gold coins In this column")
            display()
        else:
            health = health - n
            print("You found nothing. Come back later. Ghosts keep changing the location of gold in this house")
            print("GHOST: YOU WASTED YOUR TIME COMING HERE.YOU CANNOT RUN!!!")
            display()
        almirah()
    elif (choice == "2"):
        n = randint(5, 17)
        if (n % 4 == 0):
            gold = gold + n
            print("You found " + str(gold) + " gold coins In this column")
            display()
        else:
            health = health - n
            print("You found nothing. Come back later. Ghosts keep changing the location of gold in this house")
            print("GHOST: YOU WASTED YOUR TIME COMING HERE.YOU CANNOT RUN!!!")
            display()
        almirah()
    elif (choice == "3"):
        print("GHOST:YOU ARE TOO AFRAID TO SEARCH HERE")
        bedroom()
    else:
        wrong()
        almirah()


def window():
    global health
    global gold
    check()
    print("\nThere are more chances to get coins here")
    print("You are searching the window")
    sleep(4)
    n = randint(1, 40)
    if (n % 5 == 0):
        print("you got " + str(n) + " gold coins while searching window panes")
        n = n % 3
        gold = gold + n
        display()
    else:
        print("YOU were ATTACKED BY GHOST")
        health = health - n
        display()
    bedroom()


def gardenchoice():
    print(
        "\nThere is \n1.Apple tree\n2.Marigold flowers\n3.YEah! I can jump the fence(RISKY OPTION)\n4.Back to lobby.\nEnter your choice:")
    choice = (input())
    return choice


def garden():
    global health
    global gold
    check()
    print("WOW!There is a lovely garden here. We need to find something here Soon before he comes and kill me!")
    choice = gardenchoice()
    if (choice == "1"):
        n = randint(1, 9)
        if (n % 2 == 0):
            print("You found " + str(n) + " Gold coins here")
            gold = gold + n
            display()
        else:
            print("A Wild dog came from no where and attacked you!")
            health = health - n
            display()
        garden()
    elif (choice == "2"):
        n = randint(1, 14)
        if (n % 3 == 0):
            print("You found " + str(n) + " Gold coins here")
            gold = gold + n
            display()
        else:
            print("A Wild snake came from no where and attacked you!")
            health = health - n
            display()
        garden()
    elif (choice == "3"):
        print("It is too risky too jump")
        print("YOU ARE EXAMINING THE FENCE")
        sleep(2)
        print(
            "there is electric current in this fence.OH SHIT! THERE IS GHOST BEHIND YOU. YOU NEED TO JUMP OR GHOST GONNA KILL YOU!")
        n = randint(1, 9)
        if (n % 3 == 0):
            print("HEll YEAH! I survived!")
            win()
        else:
            print("YOU GOT TRAPPED IN FENCE AND ELECTRIC CURRENT KILLED YOU!")
            sleep(2)
            print("SORRY LITTLE WARRIOR.")
            kill()
    elif (choice == "4"):
        lobby()
    else:
        print("Ghost attacked you because you tried a wrong choice")
        wrong()
        garden()


def bathroomchoice():
    print("There is a \n1.bathtub\n2.Shower Area\n3.ManHole \n4.Back to lobby.\nEnter your choice")
    choice = (input())
    sleep(1)
    display()
    return choice


def bathroom():
    global health
    global gold
    check()
    print("THERE IS A SMALL BATHROOM HERE.NEED TO FIND GOLD QUICK")
    choice = bathroomchoice()
    if choice == "1":
        n = randint(1, 9)
        if (n % 2 == 0):
            print("You found " + str(n) + " Gold coins here")
            gold = gold + n
            display()
        else:
            print("A unknown animal tried to kill you in water!")
            health = health - n
            display()
        bathroom()
    elif (choice == "2"):
        n = randint(1, 14)
        if (n % 3 == 0):
            print("You found " + str(n) + " Gold coins here")
            gold = gold + n
            display()
        else:
            print("You slipped in shower area!")
            health = health - n
            display()
        bathroom()
    elif (choice == "3"):
        n = randint(1, 19)
        if (n % 4 == 0):
            print("You found " + str(n) + " Gold coins here")
            gold = gold + n
            display()
        else:
            print("A wild animal tried to pull you in that man hole!")
            health = health - n
            display()
        bathroom()
    elif (choice == "4"):
        lobby()
    else:
        print("Ghost attacked you because you tried a wrong choice")
        wrong()
        bathroom()


# game control from here
print("LAZY CODER(ARPIT SHARMA) PRESENTS:")
print("|  |   |  |  -----  |    |   ____    ___")
print("|  |   |  | |     | |    |  |       |")
print("|   ---   | |     | |    |  |____   |")
print("|         | |     | |    |       |   ---")
print("|   ---   | |     | |    |       |  |")
print("|  |   |  | |     | |    |       |  |")
print("|  |   |  |  -----   ____    ____|  |___")
print("\n\n ESCAPE!")
start()
