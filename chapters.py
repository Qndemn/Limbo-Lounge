import time
import random
import sys
import utils
import bar
import characters
import drinks
import combat

in_bar = True

def chapter_select():
    utils.slow_print("\n\n[-----===== CHAPTER SELECT =====-----]")
    utils.slow_print("\n1. Introduction")
    utils.slow_print("\n2. Chapter 1: Welcome to the TSO")
    choice = input("\nWhich chapter do you want to play? 1 or 2? ")
    if choice == "1":
        start()
        chapter_1()
    elif choice == "2":
        chapter_1()
    elif choice == "99":
        magical_fairyland()

def start():
    global sanity
    utils.slow_print("...where am I?")
    time.sleep(2)
    utils.slow_print("\n...")
    time.sleep(2)
    utils.slow_print("\nHello? Anyone?")
    time.sleep(1)
    utils.slow_print("\n...")
    time.sleep(1)
    utils.slow_print("\nGet up?")
    input("\ny/n ")
    utils.slow_print("of course I'm getting up.")
    time.sleep(1)
    utils.slow_print("\n< !HELLO THERE! >")
    time.sleep(2)
    utils.slow_print("\n...")
    time.sleep(1)
    utils.slow_print("\n< !WELL? RESPOND! >")
    utils.slow_print("\nAsk a question?")
    choice = input("y/n ")
    if choice == "y":
        while utils.sanity > 0:
          utils.slow_print("What do you want to ask? \n1. Who are you? \n2. Where am I? \n3. Am I... Dead? \n4. Exit")
          question = input("1, 2, 3 or 4? ")
          if question == "1":
              utils.slow_print("< !I'M AVICE! SHORT FOR AVARICE! >")
          if question == "2":
              utils.slow_print("< !YOU, MY FRIEND, ARE IN THE TSO! >")
              utils.slow_print("< !BUT WE JUST CALL IT THE LIMBO LOUNGE! >")
          if question == "3":
              utils.slow_print("< !! >\n< !...! >\n< !...Yes! >\n< !YES, YOU ARE.! >")
          if question == "4":
              break
    if choice == "n":
        utils.slow_print("< !NOT A TALKER, EH? >")
    utils.slow_print("\n...")
    utils.slow_print("... How do I leave?")
    time.sleep(1)
    utils.slow_print("< !BAD NEWS, KID! >")
    time.sleep(2)

def chapter_1():
    global money, drunkenness, charm
    utils.slow_print("\n\n-==== WELCOME TO TSO ====-")
    utils.slow_print("\nA game by Qndemn")
    utils.slow_print("\nChapter 1: Welcome to the TSO")
    time.sleep(2)
    utils.slow_print("\n< !SO, KID! LEMME TELL YA WHAT THIS ALL STANDS FOR! >")
    utils.slow_print("\n< !T.S.O STANDS FOR THE STAY-OVER! >")
    time.sleep(1)
    utils.slow_print("\nAsk why?")
    choice = input("y/n ")
    if choice == "y":
        utils.slow_print("\n< !BECAUSE YOU AIN'T LEAVING ANYTIME SOON! >")
    else:
        utils.slow_print("\n< ... >")
    
    utils.slow_print("\n< !ANYWAYS, LET ME EXPLAIN WHAT THIS PLACE IS ALL ABOUT! >")
    time.sleep(1)
    utils.slow_print("\n< !THE TSO IS PRETTY MUCH A...! >\n< !REALLY NICE BAR? >\n< !YEAH, THAT'S ABOUT RIGHT! >")
    time.sleep(2)
    utils.slow_print("\n< !WELL... GOOD LUCK! >\n< !OH, AND SOME ADVICE...! >\n< !WATCH YOUR POCKETS! >")
    
    utils.money -= 15
    utils.slow_print(f"\nMoney - 15 (Balance: ${utils.money})")
    time.sleep(2)
    
    while True:
        utils.slow_print(f"\nMoney: ${utils.money} | Drunkenness: {utils.drunkenness} | Charm: {utils.charm}")
        choice = input("\n\nHere are your options: \n1. Go to the counter \n2. Talk with others \n3. Search the floor \n4. Exit Game\n> ")
        
        if choice == "1":
          bar.bars()
        elif choice == "2":
            characters.dating()
        elif choice == "3":
            if characters.found_resotte == "active":
                characters.found_resotte = "found"
                utils.slow_print("\nYou found Resotte's ammo.")
                utils.integrity_check()
            else:
              if random.random() > 0.8:
                  found = random.randint(5, 10)
                  utils.money += found
                  utils.slow_print(f"\nYou found ${found} on the floor!")
              else:
                utils.slow_print("\nNothing but dust.")

        elif choice == "4":
            break
def magical_fairyland():
    utils.slow_print("\n\n[-----===== MAGICAL FAIRYLAND =====-----]")
    utils.slow_print("\nThis is a dev testing place, for new characters, and... jokes")
    utils.slow_print("\n*Am ThE hEaVy FrOm TeAm FoRtReSs 2*")
    utils.slow_print("\n*Am BiG sTrOnG rUsSiAn MaN*")
    utils.slow_print("\n\nℚ Okay, enough of the heavy from tf2 being the heavy from tf2. ℚ")
    utils.slow_print("\n\nℚ Let's give a big hand to Vous! ℚ")
    utils.slow_print("\n\n\n\n## hey, buddy ol' friend ol' pal! ##")
    utils.slow_print("\n## listen... I'm in a bit of a tight spot... ##")
    utils.slow_print("\n## couldja lend me some cash? ##")
    choice = input("\n\nLend him some cash? y/n ")
    if choice in ["y", "yes"]:
        utils.slow_print("\n## another sucker. sayonara, dumbass! ##")
        utils.money -= 100
        utils.slow_print(f"\nMoney - 100 (Balance: ${utils.money})")
    elif choice in ["n", "no"]:
        utils.slow_print("\n## ugh. where do these smart people keep coming from? ##")
    else:
        utils.slow_print("\n## ... ##")
    time.sleep(2)
    utils.slow_print("\n\nℚ More jocks (or jokes, as you moderners say): ℚ")
    utils.slow_print("\n\n//Watchout!TheScout'soutandaboutRunningaroundBringingbonksrightdowntoyourscalp(Bonk)Doyouevenknowwhoyou'retalkingtohere?I'mastreakofgreasedlightningKeepfightingforyearsI'mastunner,numberonerun-and-gunnerMybeatsbringtheheat'causeI'masweetdoublejumperYourfinger'sonthetriggerbutbeforeYougettopullitI'lltakeasipoffizzandI'llgowhizzingpastyourbulletsIamonitlikearocketona coursetofreakin'poundyaCallmesupersonic'causeI'mRunningringsaroundyaI'madabhandwithasandmanI'mthebaddestinthebadlandsI'maspeedfreakonakillstreakSeeablurthenit'sbangbang\\")
    time.sleep(5)
    utils.slow_print("ℚ 5 second should be enough time to process all that information, right? ℚ")