import random
import time
import utils
from drinks import ALL_DRINKS, comments
drink = "nothing"
in_bar = True
drink_heal = False
def bars():
    global drunkenness, charm, money, in_bar, drink
    if in_bar:
        utils.slow_print("\n*Hey pal.*")
        utils.slow_print("\n*You seem new. I know just what you need...*")
        time.sleep(2)
        utils.slow_print("\n*The TERMINAL JOLT!*\n*Might wake you up a bit.*\n*On the house.*")
        drink_choice = input("\nAccept the drink? y/n ").strip().lower()
        if drink_choice in ["y", "yes"]:
          utils.slow_print("\nYou take a sip of the drink. \nThe taste starts with a metallic, coppery zing.")
          utils.slow_print("Then, a deep, syrupy bitterness similar to over-extracted espresso washes over your palate.")
          utils.slow_print("It leaves you off with a jolt of peppermint and blue rasberry.")
          utils.drunkenness += 20
          utils.charm += 5
          utils.slow_print("\nDrunkenness +20 | Charm +5")
          in_bar = False # Next time they visit, they get the menu
        else:
            utils.slow_print("\n*Not a drinker, eh? Well, you ain't gonna last long here with that attitude, kid.*")
            in_bar = False
    else:
        utils.slow_print("\n*Back so soon? You want a drink?*")
        daily_menu = random.sample(ALL_DRINKS, 3)
        for i, d in enumerate(daily_menu, 1):
            utils.slow_print(f"{i}. {d['name']} - ${d['cost']}")       
        utils.slow_print(f"\nDrunkeness: {utils.drunkenness} | Charm: {utils.charm} | Money: ${utils.money}")
        drink_choice = input("\nWhich drink? (1, 2, 3 or 'n'): ")
        if drink_choice in ["1", "2", "3"]:
            selected = daily_menu[int(drink_choice)-1]
            if utils.money >= selected['cost']:
                drink = selected['name']
                utils.money -= selected['cost']
                utils.drunkenness += selected['drunk']
                utils.charm += selected['charm']
                utils.slow_print(f"\nMoney - {selected['cost']} (Balance: ${utils.money})")
                utils.slow_print(f"\nDrunkenness +{selected['drunk']} | Charm +{selected['charm']}")
                utils.slow_print(f"\n{selected['sip']}")
                comment = random.choice(comments).format(drink=selected['name'])
                utils.slow_print(f"\nA patron nods: '{comment}'")
                drink_heal = True
            else:
                utils.slow_print("\n*The bartender sighs.* 'You're short on cash.'")