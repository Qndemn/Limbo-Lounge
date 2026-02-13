import time
import sys
def slow_print(text, delay=0.04):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()
sanity = 100
money = 350
drunkenness = 0
charm = 50
bar = True

