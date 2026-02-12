from utils import slow_print, sanity, money, drunkenness, charm
import random
import time
from bar import drink
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
