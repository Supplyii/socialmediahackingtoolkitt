import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random

os.system("mode con:cols=160 lines=60")
os.system("color 3")
def start():
    print('''
     ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄        ▄████  ██▀███   ▄▄▄       ███▄ ▄███▓   
    ▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄     ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒   
    ▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░   
    ░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██    
    ░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒   
    ░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░ ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░   
     ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░   
     ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒   ░ ░   ░   ░░   ░   ░   ▒   ░      ░      
     ░           ░       ░                 ░  ░      ░    ░           ░  ░       ░      bruteforce -- [WINDOWS EDITION]

    Version: 0.1.1
    
    https://github.com/redKatz
    https://www.instagram.com/katz.py

    [vpn support for windows has not yet been added, so if you want make sure you are using a vpn]                                                                                    
    '''
    )
    os.system("")
    print("\n\nthe author assumes no responsability for how this content will be used\n=======================================================================\n\n")
    sceltadisc = input("\n\nUse this content for educational purposes only? [yes/no]: ")
    if sceltadisc == "yes":
        print("\n")
        os.system("")
    else:
        exit()

def acquisizione():
    while True:
        if veri_break == "si":
            break
        USER = ""
        USER = input('\nEnter Instagram Username to bruteforce: ')
        wl = input("\nEnter world list name: ")
        sleepp = int(input("\nInsert sleep time for login [Raccomanded 900(15min)]: "))
        while True:
            sub.call("clear")
            procedere = input("Username to bruteforce = "+USER+"\n\nWordlist = "+wl+"\n\nSleep time = "+str(sleepp)++"\n\nProoceding? [y/break/modify]: ")
            if procedere == "y":
                veri_break = "si"
                break
            elif procedere == "modify":
                print("\nReturn...")
                break
            elif procedere == "break":
                exit()
            else:
                passw
