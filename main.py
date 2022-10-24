import os
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
elif systemis == "Arch":
    arch()
elif systemis == "Termux":
    termux()
elif systemis == "Windows":
    termux()