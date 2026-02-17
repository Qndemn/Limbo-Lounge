from email import utils
import utils
import random
import time
import bar
def training():
    global sanity, charm, money
    mercy_points = 0
    drinks = True
    charm = True
    compliment = True
    vexer_sanity = 100
    utils.slow_print("\n\n[-----===== TRAINING =====-----]")
    utils.slow_print("\nYou take up Vexer's offer to train you in combat.")
    time.sleep(2)
    utils.slow_print(f"\nVexer's sanity: {vexer_sanity} | Your sanity: {utils.sanity}")
    while utils.sanity > 0 and vexer_sanity > 0:
        utils.slow_print("\n1. Fight \n2. Act \n3. Item \n4. Mercy")
        choice = input("\nWhat will you do? 1, 2, 3 or 4? ")
        if choice == "1":
            damage = random.randint(10, 25)
            for rounds in range(5):
                time.sleep(0.3)
                utils.slow_print("\nBAM! ")
            vexer_sanity -= damage
            utils.slow_print(f"\nYou strike Vexer, dealing {damage} damage!")
            utils.slow_print("//Woah, kid. Quite the punch you've got there.\\")
            if vexer_sanity <= 0:
                utils.slow_print("\n//...\\")
                utils.slow_print("\n//...\\")
                utils.slow_print("\n//...I... didn't know you had it in ya, kid.\\")
                utils.slow_print("\nVexer died! Money + 100")
                utils.money += 100
        elif choice == "2":
            utils.slow_print("\nChoose: \n1. Offer a drink \n2. Compliment \n3. Charm")
            act_choice = input("\n1, 2 or 3? ")
            if act_choice == "1":
                utils.slow_print(f"\nYou offer Vexer a sip of {bar.drink}")
                if bar.drink == "The Limbo Tonic":
                    if drinks:
                      utils.slow_print("\n//How'd you know that's my favorite? Thanks, kid.\\")
                      drinks = False
                      mercy_points += 1
                    else:
                      utils.slow_print("\n//Oof. I shouldn't drink too much.\\")
                else:
                    utils.slow_print("\n//Thanks, kid. But this ain't really my favorite.\\")
            elif act_choice == "2":
                if compliment:
                  utils.slow_print("\nYou compliment Vexer on his fighting skills.")
                  utils.slow_print("//Heh. You're not so bad yourself, kid.\\")
                  compliment = False
                else:
                  utils.slow_print("\n//You've already complimented me, kid.\\")
            elif act_choice == "3":
                if charm:
                  utils.slow_print("\nYou try to charm Vexer.")
                  if random.random() < (0.1 + utils.charm / 100):
                      utils.slow_print("//...Heh. Charm ain't gonna work on me, pal. Good try though.\\")
                      mercy_points += 1
                  else:
                      utils.slow_print("//Eh. Trying to charm me, eh? Ha!\\")
                else:
                    utils.slow_print("\n//You've charmed me plenty, pal.\\")
            elif act_choice == "4":
                choice = input("\n1. Mercy\n2. Flee")
                if choice == "1":
                  if mercy_points >= 3:
                      utils.slow_print("\n//So, you chose to spare me. Kid, you're too good for this place.\\")
                      vexer_sanity = 0
                  else:
                      utils.slow_print("\n//Don't think you can get out of training THAT easy.\\")
                elif choice == "2":
                  utils.slow_print("\n//Hm? Okay, I get it. You want a break. You better come back to training!\\")
                  break
                else:
                    utils.slow_print("\n//We're supposed to be training, pal. Let's keep it up.\\")
            elif act_choice == "3":
              if bar.drink_heal:
                  utils.slow_print("\nYou take a sip of your drink to heal yourself.")
                  heal_amount = random.randint(15, 30)
                  sanity += heal_amount
                  utils.slow_print(f"\nYou regain {heal_amount} sanity!")
                  bar.drink_heal = False
              else:
                  utils.slow_print("\nYou have no items to use!")