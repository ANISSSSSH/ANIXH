import platform
import os
import time
print('\n\x1b[1;37m\x1b[1;96m>>\x1b[1;97m CHECKING FOR UPDATES \x1b[1;37m')
bit = platform.architecture()[0]
if bit == '64bit':
    print('\x1b[1;37m\x1b[1;96m>>\x1b[1;97m 64 BIT FOUND \x1b[1;37m')
if bit == '32bit':
    print('\x1b[1;37m\x1b[1;96m>>\x1b[1;97m 32 BIT FOUND \x1b[1;37m')
    print('\x1b[1;96m>>\x1b[1;97m STARTING \x1b[1;37m')
os.system('git pull --quiet')
os.system('python SOURCE/data.py')