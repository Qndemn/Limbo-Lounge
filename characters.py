from utils import slow_print
import random
import time
from bar import bars
from chapters import chapter_select
from bar import drink
relationships = {"Vexer": 0, "Jackson Voe": 0, "Rsot": 0, "ZiZ": 0} 
def dating():
    upgrade = 0.1 + charm / 100
    slow_print("\n\n[-----===== BAR TALK =====-----]")
    slow_print("\nWho do you want to talk to? ")
    slow_print(f"\n1. Vexer | Relationship: {relationships['Vexer']} \n2. Jackson Voe | Relationship: {relationships['Jackson Voe']} \n3. Rsot | Relationship: {relationships['Rsot']} \n4. ZiZ | Relationship: {relationships['ZiZ']}")
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
                  drunkenness += 10
                  relationships["Vexer"] += 15
                  slow_print("\nRelationship with Vexer +15")
                  slow_print("\nDrunkenness +10")
              else:
                  slow_print("\n//Ah... Not your favorite, huh? I respect that.\\")
                  relationships["Vexer"] += 15
                  slow_print("\nRelationship with Vexer +15")
        elif relationships["Vexer"] >= 40:
              slow_print("\n//Kid, you need to learn to fight if you want to last a second here.\\")
              slow_print("//...How about training? Maybe sometime later...\\")
              slow_print("\nVexer offers to train you in combat. Do you accept? y/n ")
              choice = input().strip().lower()
              if choice in ["y", "yes"]:
                  slow_print("\nYou agree to train on a later date.")
                  relationships["Vexer"] += 10
                  slow_print("\nRelationship with Vexer +10")
              else:
                  slow_print("\n//Ah... Not your thing, huh? I get it.\\")
                  relationships["Vexer"] += 10
                  slow_print("\nRelationship with Vexer +10")
        elif relationships["Vexer"] == 50:
              slow_print("\nThis is nice, ain't it? Been a while since I've had someone to talk to.\\")
              relationships["Vexer"] = 100
        elif relationships["Vexer"] == 100:
              slow_print("\n//Hey, pal. I know this place can be rough, but I'm glad we got to know each other.\\")
              slow_print("\n//If you ever need anything, just ask. I'll have your back.\\")
              choice = input("\n//About that training session... Ready to start? y/n ").strip().lower()
              if choice in ["y", "yes"]:
                  training()
              else:
                  slow_print("\n//No rush, pal. Whenever you're ready.\\")
def training():
    global sanity, charm, money
    mercy_points = 0
    drinks = True
    charm = True
    compliment = True
    vexer_sanity = 100
    slow_print("\n\n[-----===== TRAINING =====-----]")
    slow_print("\nYou take up Vexer's offer to train you in combat.")
    time.sleep(2)
    slow_print(f"\nVexer's sanity: {vexer_sanity} | Your sanity: {sanity}")
    while sanity > 0 and vexer_sanity > 0:
        slow_print("\n1. Fight \n2. Act \n3. Item \n4. Mercy")
        choice = input("\nWhat will you do? 1, 2, 3 or 4? ")
        if choice == "1":
            damage = random.randint(10, 25)
            for rounds in range(5):
                time.sleep(0.3)
                print("BAM! ", end="")
            vexer_sanity -= damage
            slow_print(f"\nYou strike Vexer, dealing {damage} damage!")
            slow_print("//Woah, kid. Quite the punch you've got there.\\")
        elif choice == "2":
            slow_print("\nChoose: \n1. Offer a drink \n2. Compliment \n3. Charm")
            act_choice = input("\n1, 2 or 3? ")
            if act_choice == "1":
                slow_print(f"\nYou offer Vexer a sip of {drink}")
                if drink == "The Limbo Tonic":
                    if drinks:
                      slow_print("\n//How'd you know that's my favorite? Thanks, kid.\\")
                      drinks = False
                      mercy_points += 1
                    else:
                      slow_print("\n//Oof. I shouldn't drink too much.\\")
                else:
                    slow_print("\n//Thanks, kid. But this ain't really my favorite.\\")
            elif act_choice == "2":
                if compliment:
                  slow_print("\nYou compliment Vexer on his fighting skills.")
                  slow_print("//Heh. You're not so bad yourself, kid.\\")
                  compliment = False
                else:
                  slow_print("\n//You've already complimented me, kid.\\")
            elif act_choice == "3":
                if charm:
                  slow_print("\nYou try to charm Vexer.")
                  if random.random() < (0.1 + charm / 100):
                      slow_print("//...Heh. Charm ain't gonna work on me, pal. Good try though.\\")
                      mercy_points += 1
                  else:
                      slow_print("//Eh. Trying to charm me, eh? Ha!\\")
                else:
                    slow_print("\n//You've charmed me plenty, pal.\\")
            elif act_choice == "4":
                if mercy_points >= 3:
                    slow_print("\n//So, you chose to spare me. Kid, you're too good for this place.\\")
                    vexer_sanity = 0
                else:
                    slow_print("\n//We're supposed to be training, pal. Let's keep it up.\\")
