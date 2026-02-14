import time
import sys
import os
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

integrity_count = 0

def integrity_check():
    global integrity_count
    if not os.path.exists("do_not_delete.txt"):
        integrity_count += 1
        if integrity_count == 1:
          slow_print("\n\nℚ HEY KID! STOP PIRATING MY PIRATED PROPERTY")
          slow_print("\nℚ I'm not earning money for this anyhoo, but I would still like you to stop hacking my files")
          slow_print("\nℚ Because... uh... would you believe me if I told you that the code is so badly made that if you delete a single thing it'll all come crashing down?")
          slow_print("\n\nℚ Well... I'm late for my 'therapy' with my very real 'therapist' so byeℚ ")
        if integrity_count == 2:
            slow_print("\n\nℚ Pal, how did you think deleting this a SECOND TIME would help you? ℚ")
            slow_print("\nℚ You just thought: 'oh, the devs are incompetent, after the first crash, it won't happen again' ℚ")
            slow_print("\nℚ Or maybe you thought I'd say something funny. ℚ")
            time.sleep(2)
            slow_print("\nℚ ... ℚ")
            slow_print("\nℚ 'something funny' ℚ")
        if integrity_count == 3:
            slow_print("\nℚ what kind of person deletes a file then reinstalls it then deletes it then reinstalls it then deletes it again ℚ")
            slow_print("\nℚ ... ℚ")
        else:
            slow_print("\nℚ Let's just get to the point. ℚ")
        sys.exit()