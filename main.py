import time
import random
import sys

sanity = 100

def slow_print(text, delay=0.1):
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
        slow_print()

start()