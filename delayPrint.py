import time
import sys

text_speed = 0.03

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(text_speed)
