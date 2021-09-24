# digital_stream.py
#   This program emulates a screensaver in the style of the Matrix movie's visuals.
# by: Scott Gordon

import random
import shutil
import sys
import time

MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAM_CHARS = ['0', '1']

# Density can range from 0.0 to 1.0
DENSITY = 0.02

WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1  # To prevent newline

MATRIX_GREEN = '\033[92m'

print('***** Digital Stream *****')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    columns[i] = random.randint(
                        MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)

            if columns[i] > 0:
                print(MATRIX_GREEN + random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()
        sys.stdout.flush()  # Make sure text appears on the screen.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()  # Exit with Ctrl-C
