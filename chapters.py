import time
import random
import sys
from utils import slow_print
from bar import bars
from characters import dating, training
from chapters import chapter_select, start, chapter_1

sanity = 100
money = 350
drunkenness = 0
charm = 50
bar = True

drink = "nothing"
relationships = {"Vexer": 0, "Jackson Voe": 0, "Rsot": 0, "ZiZ": 0} 

ALL_DRINKS = [
    {
        "name": "The Limbo Tonic", "cost": 25, "drunk": 15, "charm": 10,
        "sip": "A silver colour similar to liquid chrome, with a bubbly, fizzing sensation. \nTaste: A sharp, citrusy flavor with a strange metallic aftertaste."
    },
    {
        "name": "Shadow-Oak Stout", "cost": 20, "drunk": 25, "charm": 5,
        "sip": "Colour: Deep, pitch black with a thick tan foam that never goes away. \nTexture: It feels syrupy and full-bodied, makes you feel 'heavy' inside. \nTaste: Smokey and earthy, like burnt caramel and wet forest soil after a rainstorm."
    },
    {
        "name": "Ether Absinthe", "cost": 30, "drunk": 20, "charm": 15,
        "sip": "Colour: A neon violet that glows in the bar's lights. \nTexture: It is oily and slick, covering the throat with a cooling film. \nTaste: An intense Anise mixed with a bittersweet herbal punch and a hint of lavender."
    },
    {
        "name": "The Infernum", "cost": 30, "drunk": 20, "charm": 5,
        "sip": "Colour: A smoldering, translucent amber. \nTexture: Warm and thin, leaving a trail of heat in the chest. \nTaste: Toasted cinnamon, charcoal, and a dry, lingering spice."
    },
    {
        "name": "The Polaris", "cost": 30, "drunk": 10, "charm": 20,
        "sip": "Colour: Perfectly clear with a single silver light at the bottom. \nTexture: Crisp and bitingly cold, like mountain water. \nTaste: Sharp peppermint, ozone, and a faint hint of sugar."
    },
    {
        "name": "Copper-Line Lager", "cost": 15, "drunk": 15, "charm": 5,
        "sip": "Colour: A dull, standard gold with moderate carbonation. \nTexture: Light and watery, easy to drink in large gulps. \nTaste: Bitter hops and a metallic tang, reminiscent of a city pub."
    }
]

comments = [
    "Hey, pal. Nice choice on the {drink}. I've been drinking those since the 40s.",
    "Ah, the {drink}! A classic. It's the only thing that tastes 'right' in this place.",
    "The {drink}? Bold choice. Most people can't handle the kick.",
    "The {drink} is a favorite around here. Keeps the quiet from getting too loud.",
    "The {drink}. Good pick. It reminds me of a place I used to know.",
    "You can't go wrong with a {drink}. It's got character, just like this bar.",
    "The {drink}? Now that's a drink with a story.",
    "Ah, the {drink}. It's got a way of growing on you after a while.",
    "The {drink} is a solid choice. Helps you forget where you are for a bit.",
]

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

def chapter_1():
    global money, drunkenness, charm
    bar = True # Set to True so first interaction uses the "New pal" script
    
    time.sleep(2)
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
            dating()
        elif choice == "3":
            if random.random() > 0.8:
                found = random.randint(5, 10)
                money += found
                slow_print(f"\nYou found ${found} on the floor!")
            else:
                slow_print("\nNothing but dust.")

        elif choice == "4":
            break

chapter_select()
