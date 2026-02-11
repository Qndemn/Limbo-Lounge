import time
import random
import sys

sanity = 100
money = 350
drunkenness = 0
charm = 50

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
    "The {drink}. Good pick. It reminds me of a place I used to know."
]

def slow_print(text, delay=0.07):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def dating():
    global relationships, charm, money, drunkenness, sanity
    upgrade = 0.1 + charm / 100
    slow_print("\n\n[-----===== BAR TALK =====-----]")
    slow_print("\nWho do you want to talk to? ")
    slow_print(f"\n1. Vexer {relationships["Vexer"]} \n2. Jackson Voe {relationships["Jackson Voe"]} \n3. Rsot {relationships["Rsot"]} \n4. ZiZ {relationships["ZiZ"]}")
    choice = input("\n1, 2, 3 or 4? ")
    if choice == "1":
        slow_print("\nYou approach Vexer.")
        if relationships["Vexer"] == 0:
          upgrade = 0.1 + charm / 100
          if random.random() < upgrade:
            slow_print("\n//Hmph. You're a good guy. Hell, not like you're anything special.\\")
            relationships["Vexer"] += 5
        else:
            slow_print("\n//...Buzz off, kid. Ain't nobody have time for greens like you.\\")
    elif relationships["Vexer"] == 5:
        if random.random() < upgrade:
                slow_print("\n//Pal, you seem nice. Keep your head low, and you might learn to be tough.\\")
                relationships["Vexer"] += 10
        else:
                slow_print(f"\n//...Maybe later, pal. I've got a Limbo Tonic with my name on it.\\")
    elif relationships["Vexer"] == 15:
        slow_print("\n//Hey, you've met Avice, huh? Shame. Took some money, eh? Ah, I've gotcha covered.\\")
        slow_print("\nVexer gives you $20.")
        money += 20
        relationships["Vexer"] += 10
    elif relationships["Vexer"] == 25:
            slow_print("\n//Ain't you just a little ray of sunshine? Not many folks 'round here want to be too friendly.\\")
            slow_print("\n//Ha! Ya know, how about we grab a drink together? My treat.\\")
            drink_choice = input("\nAccept the drink? y/n ").strip().lower()
            if drink_choice in ["y", "yes"]:
                slow_print("\nYou and Vexer share a drink. You feel a little closer to him.")
                relationships["Vexer"] += 15
                charm += 10
                slow_print("\nRelationship with Vexer +15 | Charm +10")
            else:
                slow_print("\n//Ah... Not your favorite, huh? I respect that.\\")
                relationships["Vexer"] += 5
                charm += 5
                slow_print("\nRelationship with Vexer +5 | Charm +5")
    elif relationships["Vexer"] >= 40:
            slow_print("\n//Kid, you need to learn to fight if you want to last a second here.\\")
            slow_print("//...How about training? Maybe sometime later...\\")
            slow_print("\nVexer offers to train you in combat. Do you accept? y/n ")
            choice = input().strip().lower()
            if choice in ["y", "yes"]:
                slow_print("\nYou agree to train on a later date.")
                relationships["Vexer"] += 20
                charm += 10
                slow_print("\nRelationship with Vexer +20 | Charm +10")
            else:
                slow_print("\n//Ah... Not your thing, huh? I get it.\\")
                relationships["Vexer"] += 10
                charm += 5
                slow_print("\nRelationship with Vexer +10 | Charm +5")
    elif relationships["Vexer"] >= 50:
            slow_print("\nThis is nice, ain't it? Been a while since I've had someone to talk to.\\")
            relationships["Vexer"] = 100
    elif relationships["Vexer"] == 100:
            slow_print("\n//Hey, pal. I know this place can be rough, but I'm glad we got to know each other.\\")
            slow_print("\n//If you ever need anything, just ask. I'll have your back.\\")

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
        choice = input("\n\nHere are your options: \n1. Go to the counter \n2. Talk with others \n3. Search the floor \n4. Exit Game\n> ")
        
        if choice == "1":
            if bar:
                slow_print("\n*Hey pal.*")
                slow_print("\n*You seem new. I know just what you need...*")
                time.sleep(2)
                slow_print("\n*The TERMINAL JOLT!*\n*Might wake you up a bit.*\n*On the house.*")
                drink_choice = input("\nAccept the drink? y/n ").strip().lower()
                if drink_choice in ["y", "yes"]:
                    slow_print("\nYou take a sip of the drink. \nThe taste starts with a metallic, coppery zing.")
                    slow_print("Then, a deep, syrupy bitterness similar to over-extracted espresso washes over your palate.")
                    slow_print("It leaves you off with a jolt of peppermint and blue rasberry.")
                    drunkenness += 20
                    charm += 5
                    slow_print("\nDrunkenness +20 | Charm +5")
                    bar = False # Next time they visit, they get the menu
                else:
                    slow_print("\n*Not a drinker, eh? Well, you ain't gonna last long here with that attitude, kid.*")
                    bar = False
            else:
                slow_print("\n*Back so soon? You want a drink?*")
                daily_menu = random.sample(ALL_DRINKS, 3)
                for i, d in enumerate(daily_menu, 1):
                    slow_print(f"{i}. {d['name']} - ${d['cost']}")
                
                drink_choice = input("\nWhich drink? (1, 2, 3 or 'n'): ")
                if drink_choice in ["1", "2", "3"]:
                    selected = daily_menu[int(drink_choice)-1]
                    if money >= selected['cost']:
                        money -= selected['cost']
                        drunkenness += selected['drunk']
                        charm += selected['charm']
                        slow_print(f"\n{selected['sip']}")
                        comment = random.choice(comments).format(drink=selected['name'])
                        slow_print(f"\nA patron nods: '{comment}'")
                    else:
                        slow_print("\n*The bartender sighs.* 'You're short on cash.'")

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
