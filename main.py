import time
import random
import sys

def slow_print(text, delay=0.05):
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