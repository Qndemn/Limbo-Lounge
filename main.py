import time
import random
import sys
from utils import slow_print
from bar import bars
from characters import dating, training
from chapters import chapter_select, start, chapter_1

sanity = 100
money = 350
drunkenness = 0
charm = 50
bar = True

if __name__ == "__main__":
    slow_print("\n\n[-----===== WELCOME TO TSO =====-----]")
    chapter_select()