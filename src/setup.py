import os
scelta = input("Wich system are you using: \n1) windows\n2) linux\n> ")
if scelta == "1":
    os.system("pip install bs4")
    os.system("pip install requests")
    os.system("pip install mechanize")
    os.system("pip install secure-smtplib")
elif scelta == "2":
    os.system("pip3 install bs4")
    os.system("pip3 install requests")
    os.system("pip3 install mechanize")
    os.system("pip3 install secure-smtplib")
print("Run python smh.py to run the program")