import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
os.system("clear")
print('''
Which system are you using

\n1) Linux - Debian\n2) Linux - Arch\n3) Termux\n4) Windows
''')
sys = input("\n> ")

if sys == "1":
    sistema = "Debian"
elif sys == "2":
    sistema = "Arch"
elif sys == "3":
    sistema = "Termux"
elif sys == "4":
    sistema = "Windows"

f = open("whosys.py", "a")
f.write("\nsystemis = '"+sistema+"'")
f.close()
os.system("pip3 install instaloader")

if sys == "1":
    print(color.YELLOW+'''\nIMPORTANT'''+color.END+'''

    -to run this tool you need to install "windscribe-cli"

    -the installation process may differ, so follow this
    guide and make sure you install the program correctly --> Debian['''+color.UNDERLINE+color.BLUE+'''https://www.geeksforgeeks.org/how-to-setup-vpn-on-ubuntu-linux-system-for-ip-spoofing-using-windscribe/'''+color.END+''']
                                                          --> Arch['''+color.UNDERLINE+color.BLUE+'''Install yay | yay install windscribe-cli '''+color.END+''']

    \n\n''')
if sys == "2":
    print(color.YELLOW+'''\nIMPORTANT'''+color.END+'''

    -to run this tool you need to install "windscribe-cli"

    -the installation process may differ, so follow this
    guide and make sure you install the program correctly --> Debian['''+color.UNDERLINE+color.BLUE+'''https://www.geeksforgeeks.org/how-to-setup-vpn-on-ubuntu-linux-system-for-ip-spoofing-using-windscribe/'''+color.END+''']
                                                          --> Arch['''+color.UNDERLINE+color.BLUE+'''Install yay | yay install windscribe-cli '''+color.END+''']

    \n\n''')
    input("press any key to continue")
else:
    print(color.YELLOW+'''\nSetup successfully completed'''+color.END+'''
''')
