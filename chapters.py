import time
import random
import sys
from utils import slow_print
import bar
from utils import sanity, money, drunkenness, charm
import characters
from drinks import ALL_DRINKS, comments
from combat import training

sanity = 100
money = 350
drunkenness = 0
charm = 50
bar = True

def chapter_select():
    slow_print("\n\n[-----===== CHAPTER SELECT =====-----]")
    slow_print("\n1. Introduction")
    slow_print("\n2. Chapter 1: Welcome to the TSO")
    choice = input("\nWhich chapter do you want to play? 1 or 2? ")
    if choice == "1":
        start()
        chapter_1()
    elif choice == "2":
        chapter_1()

def start():
    global sanity
    slow_print("...where am I?")
    time.sleep(2)
    slow_print("\n...")
    time.sleep(2)
    slow_print("\nHello? Anyone?")
    time.sleep(1)
    slow_print("\n...")
    time.sleep(1)
    slow_print("\nGet up?")
    input("\ny/n ")
    slow_print("of course I'm getting up.")
    time.sleep(1)
    slow_print("\n< !HELLO THERE! >")
    time.sleep(2)
    slow_print("\n...")
    time.sleep(1)
    slow_print("\n< !WELL? RESPOND! >")
    slow_print("\nAsk a question?")
    choice = input("y/n ")
    if choice == "y":
        while sanity > 0:
          slow_print("What do you want to ask? \n1. Who are you? \n2. Where am I? \n3. Am I... Dead? \n4. Exit")
          question = input("1, 2, 3 or 4? ")
          if question == "1":
              slow_print("< !I'M AVICE! SHORT FOR AVARICE! >")
          if question == "2":
              slow_print("< !YOU, MY FRIEND, ARE IN THE TSO! >")
              slow_print("< !BUT WE JUST CALL IT THE LIMBO LOUNGE! >")
          if question == "3":
              slow_print("< !! >\n< !...! >\n< !...Yes! >\n< !YES, YOU ARE.! >")
          if question == "4":
              break
    if choice == "n":
        slow_print("< !NOT A TALKER, EH? >")
    slow_print("\n...")
    slow_print("... How do I leave?")
    time.sleep(1)
    slow_print("< !BAD NEWS, KID! >")
    time.sleep(2)

def chapter_1():
    global money, drunkenness, charm
    slow_print("\n\n-==== WELCOME TO TSO ====-")
    slow_print("\nA game by Qndemn")
    slow_print("\nChapter 1: Welcome to the TSO")
    time.sleep(2)
    slow_print("\n< !SO, KID! LEMME TELL YA WHAT THIS ALL STANDS FOR! >")
    slow_print("\n< !T.S.O STANDS FOR THE STAY-OVER! >")
    time.sleep(1)
    slow_print("\nAsk why?")
    choice = input("y/n ")
    if choice == "y":
        slow_print("\n< !BECAUSE YOU AIN'T LEAVING ANYTIME SOON! >")
    else:
        slow_print("\n< ... >")
    
    slow_print("\n< !ANYWAYS, LET ME EXPLAIN WHAT THIS PLACE IS ALL ABOUT! >")
    time.sleep(1)
    slow_print("\n< !THE TSO IS PRETTY MUCH A...! >\n< !REALLY NICE BAR? >\n< !YEAH, THAT'S ABOUT RIGHT! >")
    time.sleep(2)
    slow_print("\n< !WELL... GOOD LUCK! >\n< !OH, AND SOME ADVICE...! >\n< !WATCH YOUR POCKETS! >")
    
    money -= 15
    slow_print(f"\nMoney - 15 (Balance: ${money})")
    time.sleep(2)
    
    while True:
        slow_print(f"\nMoney: ${money} | Drunkenness: {drunkenness} | Charm: {charm}")
        choice = input("\n\nHere are your options: \n1. Go to the counter \n2. Talk with others \n3. Search the floor \n4. Exit Game\n> ")
        
        if choice == "1":
          bars()
        elif choice == "2":
            characters.dating()
        elif choice == "3":
            if characters.found_rsot == "active":
                characters.found_rsot = "found"
                slow_print("\nYou found Rsot's ammo.")
            else:
              if random.random() > 0.8:
                  found = random.randint(5, 10)
                  money += found
                  slow_print(f"\nYou found ${found} on the floor!")
              else:
                slow_print("\nNothing but dust.")

        elif choice == "4":
            break