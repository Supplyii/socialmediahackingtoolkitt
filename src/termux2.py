import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    OKVERDE = '\033[92m'

def ascii():

    print(bcolors.OKGREEN+'''
 _           _          '''+bcolors.WARNING+'''___'''+bcolors.OKGREEN+'''                  
(_)_ __  ___| |_ __ _  '''+bcolors.WARNING+'''/ __\''''+bcolors.OKGREEN+'''__  _ __ ___ ___ 
| | '_ \/ __| __/ _` |'''+bcolors.WARNING+'''/ _\''''+bcolors.OKGREEN+'''/ _ \| '__/ __/ _ |
| | | | \__ \ || (_| '''+bcolors.WARNING+'''/ /'''+bcolors.OKGREEN+''' | (_) | | | (_|  __/
|_|_| |_|___/\__\__,_'''+bcolors.WARNING+'''\/'''+bcolors.OKGREEN+'''   \___/|_|  \___\___|
                                                                                           
        '''
        +bcolors.ENDC)
def start():
    print(bcolors.OKGREEN+'''
 _           _          '''+bcolors.WARNING+'''___'''+bcolors.OKGREEN+'''                  
(_)_ __  ___| |_ __ _  '''+bcolors.WARNING+'''/ __\''''+bcolors.OKGREEN+'''__  _ __ ___ ___ 
| | '_ \/ __| __/ _` |'''+bcolors.WARNING+'''/ _\''''+bcolors.OKGREEN+'''/ _ \| '__/ __/ _ |
| | | | \__ \ || (_| '''+bcolors.WARNING+'''/ /'''+bcolors.OKGREEN+''' | (_) | | | (_|  __/
|_|_| |_|___/\__\__,_'''+bcolors.WARNING+'''\/'''+bcolors.OKGREEN+'''   \___/|_|  \___\___|
                                                '''+bcolors.ENDC+'''
    ['''+bcolors.OKGREEN+'''v'''+bcolors.FAIL+'''0.2.2'''+bcolors.ENDC+''']
                                                                                   
    '''+bcolors.ENDC)
    print(bcolors.WARNING+bcolors.UNDERLINE+"\n\nthe author assumes no responsability for how this content will be used\n\n"+bcolors.ENDC)
    sceltadisc = input("\n\nUse this content for educational purposes only? [yes/no]: ")
    if sceltadisc == "yes" or sceltadisc == "y":
        print("\n")
        os.system("clear")
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
