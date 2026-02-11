import time
import random
import sys

sanity = 100
money = 350
drunkenness = 0
charm = 50

def slow_print(text, delay=0.085):
    """
    Prints text character by character to simulate a typing effect.

    Args:
        text (str): The string to print slowly.
        delay (float): The time delay (in seconds) between characters.
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def chapter_select():
    slow_print("\n\n[-----===== CHAPTER SELECT =====-----]")
    slow_print("\n1. Introduction")
    slow_print("\n2. Chapter 1: Welcome to the TSO")
    choice = input("\nWhich chapter do you want to play? 1 or 2? ")
    if choice == "1":
        start()
        chapter_1()
    if choice == "2":
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
              slow_print("< !! >")
              slow_print("< !...! >")
              slow_print("< !...Yes! >")
              slow_print("< !YES, YOU ARE.! >")
          if question == "4":
              break
    if choice == "n":
        slow_print("< !NOT A TALKER, EH? >")
    slow_print("\n...")
    slow_print("... How do I leave?")
    time.sleep(1)
    slow_print("< !BAD NEWS, KID! >")

def chapter_1():
    global money, drunkenness, charm
    time.sleep(2)
    slow_print("\n\n-==== WELCOME TO TSO ====-")
    slow_print("\nA game by: Qndemn")
    slow_print("\nChapter 1: Welcome to the TSO")
    time.sleep(2)
    slow_print("\n< !SO, KID! LEMME TELL YA WHAT THIS ALL STANDS FOR! >")
    slow_print("\n< !T.S.O STANDS FOR THE STAY-OVER! >")
    time.sleep(1)
    slow_print("\nAsk why?")
    choice = input("y/n ")
    if choice == "y":
        slow_print("\n< !BECAUSE YOU AIN'T LEAVING ANYTIME SOON! >")
    if choice == "n":
        slow_print("\n< ... >")
    slow_print("\n< !ANYWAYS, LET ME EXPLAIN WHAT THIS PLACE IS ALL ABOUT! >")
    time.sleep(1)
    slow_print("\n< !THE TSO IS PRETTY MUCH A...! >")
    slow_print("\n< !REALLY NICE BAR? >")
    slow_print("\n< !YEAH, THAT'S ABOUT RIGHT! >")
    time.sleep(2)
    slow_print("\n< !WELL... GOOD LUCK! >")
    slow_print("\n< !OH, AND SOME ADVICE...! >")
    slow_print("\n< !WATCH YOUR POCKETS! >")
    slow_print("\nMoney - 15")
    money -= 15
    time.sleep(2)
    choice = input("\n\nHere are your options: \n1. Go to the counter \n2. Talk with others \n3. Search the floor \n1, 2 or 3? ")
    if choice == "1":
        slow_print("\n*Hey pal.*")
        slow_print("\n*You seem new. I know just what you need...*")
        time.sleep(2)
        slow_print("\n*The TERMINAL JOLT!*")
        slow_print("\n*Might wake you up a bit.*")
        slow_print("\n*On the house.*")
        choice = input("\nAccept the drink? y/n ").strip().lower()
        if choice in ["y", "yes"]:
            slow_print("\nYou take a sip of the drink.")
            slow_print("\nThe taste starts with a metallic, coppery zing.")
            slow_print("\nThen, a deep, syrupy bitterness similar to over-extracted espresso washes over your palate.")
            slow_print("\nIt leaves you off with a jolt of peppermint and blue rasberry, which adds a nice kick to the drink.")
            slow_print("\nDrunkenness +20")
            slow_print("\nYour vision swims. The neon lights of the bar blur together, creating a kaleidoscope of colors that dance before your eyes.")
            drunkenness += 20
            charm += 5
            slow_print("\nCharm +5")
        if choice in ["n", "no"]:
            slow_print("\n*Not a drinker, eh?*")
            slow_print("\n*Well, you ain't gonna last long here with that additude, kid.*")
            slow_print("\n*Your gonna be here a while, might as well enjoy it.*")

chapter_select()