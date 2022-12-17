import os
scelta = input("Wich system are you using: \n1) windows\n2) linux\n> ")
if scelta == "1":
    os.system("pip install bs4")
    os.system("pip install requests")
    os.system("pip install mechanize")
    os.system("pip install secure-smtplib")
    os.system("cls")
elif scelta == "2":
    os.system("pip3 install bs4")
    os.system("pip3 install requests")
    os.system("pip3 install mechanize")
    os.system("pip3 install secure-smtplib")
    os.system("clear")
print("Run python smh.py to run the program")

print("WARNING: vpn doesn't work on windwos and termux, also to use it on linux systems you have to install windscribe-cli; tutorial --> https://www.geeksforgeeks.org/how-to-setup-vpn-on-ubuntu-linux-system-for-ip-spoofing-using-windscribe/")
