from chapters import chapter_select, start, chapter_1
import os
import utils
import sys

if not os.path.exists("do_not_delete.txt"):
    utils.slow_print("\n\nℚ HEY KID! STOP PIRATING MY PIRATED PROPERTY")
    utils.slow_print("\nℚ I'm not earning money for this anyhoo, but I would still like you to stop hacking my files")
    utils.slow_print("\nℚ Because... uh... would you believe me if I told you that the code is so badly made that if you delete a single thing it'll all come crashing down?")
    utils.slow_print("\n\nWell... I'm late for my 'therapy' with my very real 'therapist' so bye")
    sys.exit()

if __name__ == "__main__":
    chapter_select()