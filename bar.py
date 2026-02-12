import random
import time
from utils import slow_print
from drinks import ALL_DRINKS, comments
drink = "nothing"
def bars():
    global drunkenness, charm, money, bar, drink
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
        slow_print(f"\nDrunkeness: {drunkenness} | Charm: {charm} | Money: ${money}")
        drink_choice = input("\nWhich drink? (1, 2, 3 or 'n'): ")
        if drink_choice in ["1", "2", "3"]:
            selected = daily_menu[int(drink_choice)-1]
            if money >= selected['cost']:
                drink = selected['name']
                money -= selected['cost']
                drunkenness += selected['drunk']
                charm += selected['charm']
                slow_print(f"\nMoney - {selected['cost']} (Balance: ${money})")
                slow_print(f"\nDrunkenness +{selected['drunk']} | Charm +{selected['charm']}")
                slow_print(f"\n{selected['sip']}")
                comment = random.choice(comments).format(drink=selected['name'])
                slow_print(f"\nA patron nods: '{comment}'")
            else:
                slow_print("\n*The bartender sighs.* 'You're short on cash.'")