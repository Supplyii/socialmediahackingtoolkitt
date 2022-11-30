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
os.system("pip3 install pyfiglet")





if sys == "1":
    os.system("echo 'php installation'")
    os.system("sudo apt-get install php")
    print(color.YELLOW+'''
                    IMPORTANT'''+color.END+'''
    To run this tool with vpn you need to install "windscribe-cli"
    The installation process may differ, so follow this
    guide and make sure you install the program correctly 
    Debian['''+color.UNDERLINE+color.BLUE+'''https://www.geeksforgeeks.org/how-to-setup-vpn-on-ubuntu-linux-system-for-ip-spoofing-using-windscribe/'''+color.END+''']
    \n    Arch['''+color.BLUE+'''Install yay | yay install windscribe-cli '''+color.END+''']
    \n\n''')
if sys == "2":
    os.system("yay -S php")
    print(color.YELLOW+'''
                    IMPORTANT'''+color.END+'''
    To run this tool with vpn you need to install "windscribe-cli"
    The installation process may differ, so follow this
    guide and make sure you install the program correctly 
    Debian['''+color.UNDERLINE+color.BLUE+'''https://www.geeksforgeeks.org/how-to-setup-vpn-on-ubuntu-linux-system-for-ip-spoofing-using-windscribe/'''+color.END+''']
    \n   Arch['''+color.BLUE+'''Install yay | yay install windscribe-cli '''+color.END+''']''')
print(color.YELLOW+'''\nSetup successfully completed'''+color.END+'''
''')
if sys == "3":
    os.system("pkg install php")
os.system("pip3 install requests")
os.system("pip3 install pyfiglet")
os.system("pip3 install colorama")
input("python3 main.py to run the program; \nPress enter to exit. ")
os.system("touch setup_ver.py")