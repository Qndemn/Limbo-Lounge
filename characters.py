import utils
import random
import time
import bar
from combat import training
found_resotte = "none"
relationships = {"Vexer": 0, "Jackson Voe": 0, "Resotte": 0, "Vous": 0}
vous_interact = True
sear_interact = False
def dating():
    global vous_interact, sear_interact
    upgrade = 0.1 + utils.charm / 100
    utils.slow_print("\n\n[-----===== BAR TALK =====-----]")
    utils.slow_print("\nWho do you want to talk to? ")
    utils.slow_print(f"\n1. Vexer | Relationship: {relationships['Vexer']} \n2. Jackson Voe | Relationship: {relationships['Jackson Voe']} \n3. Resotte | Relationship: {relationships['Resotte']}")
    if vous_interact:
        utils.slow_print(f"4. Vous | Relationship: {relationships['Vous']}")
    else:
        utils.slow_print("4. Sear | Relationship: #")
    choice = input("\n1, 2, 3 or 4? ")
    if choice == "1":
        utils.slow_print("\nYou approach Vexer.")
        if relationships["Vexer"] == 0:
          upgrade = 0.1 + utils.charm / 100
          if random.random() < upgrade:
            utils.slow_print("\n//Hmph. You're a good guy. Hell, not like you're anything special.\\")
            relationships["Vexer"] += 5
          else:
            utils.slow_print("\n//...Buzz off, kid. Ain't nobody have time for greens like you.\\")
        elif relationships["Vexer"] == 5:
          if random.random() < upgrade:
              utils.slow_print("\n//Pal, you seem nice. Keep your head low, and you might learn to be tough.\\")
              relationships["Vexer"] += 10
          else:
              utils.slow_print(f"\n//...Maybe later, pal. I've got a Limbo Tonic with my name on it.\\")
        elif relationships["Vexer"] == 15:
          utils.slow_print("\n//Hey, you've met Avice, huh? Shame. Took some money, eh? Ah, I've gotcha covered.\\")
          utils.slow_print("\nVexer gives you $20.")
          utils.money += 20
          relationships["Vexer"] += 10
        elif relationships["Vexer"] == 25:
              utils.slow_print("\n//Ain't you just a little ray of sunshine? Not many folks 'round here want to be too friendly.\\")
              utils.slow_print("\n//Ha! Ya know, how about we grab a Limbo Tonic together? My treat.\\")
              drink_choice = input("\nAccept the drink? y/n ").strip().lower()
              if drink_choice in ["y", "yes"]:
                  utils.slow_print("\nYou and Vexer share a drink. You feel a little closer to him.")
                  utils.drunkenness += 10
                  relationships["Vexer"] += 15
                  utils.slow_print("\nRelationship with Vexer +15")
                  utils.slow_print("\nDrunkenness +10")
              else:
                  utils.slow_print("\n//Ah... Not your favorite, huh? I respect that.\\")
                  relationships["Vexer"] += 15
                  utils.slow_print("\nRelationship with Vexer +15")
        elif relationships["Vexer"] == 40:
              utils.slow_print("\n//Kid, you need to learn to fight if you want to last a second here.\\")
              utils.slow_print("//...How about training? Maybe sometime later...\\")
              utils.slow_print("\nVexer offers to train you in combat. Do you accept? y/n ")
              choice = input().strip().lower()
              if choice in ["y", "yes"]:
                  utils.slow_print("\nYou agree to train on a later date.")
                  relationships["Vexer"] += 10
                  utils.slow_print("\nRelationship with Vexer +10")
              else:
                  utils.slow_print("\n//Ah... Not your thing, huh? I get it.\\")
                  relationships["Vexer"] += 10
                  utils.slow_print("\nRelationship with Vexer +10")
        elif relationships["Vexer"] == 50:
              utils.slow_print("\n//This is nice, ain't it? Been a while since I've had someone to talk to.\\")
              relationships["Vexer"] = 100
        elif relationships["Vexer"] == 100:
              utils.slow_print("\n//Hey, pal. I know this place can be rough, but I'm glad we got to know each other.\\")
              utils.slow_print("\n//If you ever need anything, just ask. I'll have your back.\\")
              choice = input("\n//About that training session... Ready to start? y/n ").strip().lower()
              if choice in ["y", "yes"]:
                  training()
              else:
                  utils.slow_print("\n//No rush, pal. Whenever you're ready.\\")
    elif choice == "2":
        utils.slow_print("\nYou approach Jackson Voe.")
        if relationships["Jackson Voe"] == 0:
            if bar.drink == "Copper-Line Lager":
                utils.slow_print("You offer him your Copper-Line Lager.")
                utils.slow_print("\n''Hm? Ah. Good stuff. Now get lost.''")
                relationships["Jackson Voe"] += 5
            else:
                utils.slow_print("\n''Get lost, kid. Unless you've got a copper-line lager for me.''")
        elif relationships["Jackson Voe"] == 5:
            utils.slow_print("\n''Damn, you're persistent. Let me drink in peace.''")
            utils.slow_print("\nJackson Voe takes a swig of his drink and goes back to staring into space.")
            relationships["Jackson Voe"] += 10
        elif relationships["Jackson Voe"] == 15:
            utils.slow_print("\n''You again? Look, kid, I'm not in the mood to chat. Just let me be.''")
            relationships["Jackson Voe"] += 10
        elif relationships["Jackson Voe"] == 25:
            utils.slow_print("\n''Kid... You don't want me around you. I know too much. Here, will this satisfy your player instincts?''")
            relationships["Jackson Voe"] = 100
            utils.slow_print("\nRelationship with Jackson Voe set to 100")
            utils.slow_print("\n''There. Now leave me be.''")
        else:
            utils.slow_print("\n ~ℂ 𝕆 𝕃 𝔻 𝕊 𝕀 𝕃 𝔼 ℕ ℂ 𝔼~", delay=0.3)
    elif choice == "3":
        utils.slow_print("\nYou approach Resotte.")
        if relationships["Resotte"] == 0:
          utils.slow_print("\n|Hey, pal!|")
          utils.slow_print("\n|You, my friend, look like you could use some money!|")
          utils.slow_print("\n|How about you do me a little favor?|")
          utils.slow_print("\n|Trust me, I'll make it worth your while.|")
          choice = input("\nDo you accept Resotte's favor? y/n ").strip().lower()
          relationships["Resotte"] += 5
          if choice in ["y", "yes"]:
              global found_resotte
              found_resotte = "active"
              utils.slow_print("\n|Great! So, I dropped my ammo somewhere around here.|")
              utils.slow_print("|If you find it, I'll give you a reward!|")
          elif choice in ["n", "no"]:
              utils.slow_print("\n|Ouch, tough crowd.|")
        elif relationships["Resotte"] == 5:
            if found_resotte == "found":
                utils.slow_print("\n|Hey, thanks pal! Here's your reward.|")
                utils.money += 85
                utils.slow_print("\nMoney +85")
                relationships["Resotte"] = 100
            else:
                utils.slow_print("\n|Any luck?|")
    elif choice == "4":
        if vous_interact:
          vous_interact = False
          utils.slow_print("\n## hey, buddy ol' friend ol' pal! ##")
          utils.slow_print("\n## listen... I'm in a bit of a tight spot... ##")
          utils.slow_print("\n## couldja lend me some cash? ##")
          choice = input("\n\nLend him some cash? y/n ").strip().lower()
          if choice in ["y", "yes"]:
            utils.slow_print("\n## another sucker. sayonara, dumbass! ##")
            utils.money -= 100
            utils.slow_print(f"\nMoney - 100 (Balance: ${utils.money})")
          elif choice in ["n", "no"]:
            utils.slow_print("\n## ugh. where do these smart people keep coming from? ##")
          else:
            utils.slow_print("\n## ... ##")
          sear_interact = True
        else:
            if sear_interact:
              sear_interact = False
              utils.slow_print("\n## uh-oh... well, bye! ##")
              utils.slow_print("\n## don't stick around this guy too long, 'kay? ##")
              time.sleep(3)
              utils.slow_print("\n\n❖ Hello, child. I see you are adjusting well? Gut. ❖")
              choice = input("Ask about Vous? y/n ").strip().lower()
              if choice in ["y", "yes"]:
                  utils.slow_print("\n❖ Ah. Vous, scampering away like always. No need for fear, he is nothing but a cowardly weasel. ❖")
              else:
                  utils.slow_print("❖ ... Ah. It seemed you were going to say something. I suppose not. ❖")
              utils.slow_print("\n❖ That is not of import at this time. ❖")
              utils.slow_print("\n❖ You appear to be finding your footing. Adjusting well, I take it. ❖")
              choice = input("Are you adjusting? y/n ").strip().lower()
              if choice in ["y", "yes"]:
                  utils.slow_print("\n❖ Vollkommen. Ensure that it remains this way. Verstanden? ❖")
              else:
                  utils.slow_print("\n❖ You seem quite hesitant, child. If you have a question, ask. ❖")
              utils.slow_print("\n\n❖ There is still much you do not understand. All in due time. ❖")
            else:
                utils.slow_print("❖ You have no need to speak with me now. Go, du idiotisches Kind. ❖")