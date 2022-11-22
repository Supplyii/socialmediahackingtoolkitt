import os
os.system("clear")
try:
    import src.setup_ver
except Exception:
    scelta_setup = input("Setup did not run properly, would you like to run it again? [y/n]: ")
    if scelta_setup == "y":
        os.chdir("src")
        os.system("python3 setup.py")
        exit()
    else:
        exit()
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
from src.linux import *
from src.termux import *
from src.arch import *
from src.windows import *
from src.whosys import systemis


if systemis == "Debian":
    linux()
    os.system("windscribe stop")
elif systemis == "Arch":
    os.system("sudo systemctl start windscribe")
    arch()
    os.system("windscribe stop")

elif systemis == "Termux":
    termux()
elif systemis == "Windows":
    windows()


