import time
import random
import sys

sanity = 100

def slow_print(text, delay=0.085):
    """
    Prints text character by character to simulate a typing effect.

    Args:
        text (str): The string to print slowly.
        delay (float): The time delay (in seconds) between characters.
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()

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
        slow_print("What do you want to ask? \n1. Who are you? \n2. Where am I? \n3. Am I... Dead?")
        question = input("1, 2 or 3? ")
        if question == "1":
            slow_print("< !I'M AVICE! SHORT FOR AVARICE! >")
        if question == "2":
            slow_print("< !YOU, MY FRIEND, ARE IN THE TSO! >")
            slow_print("< !BUT WE JUST CALL IT THE LIMBO LOUNGE! >")
        if question == "3":
            slow_print("< !! >")
            slow_print("< !...! >")
            slow_print("< !UH, YES! >")


start()