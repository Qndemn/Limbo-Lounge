from utils import slow_print, sanity, money, drunkenness, charm
import random
import time
from bar import bars, drink
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