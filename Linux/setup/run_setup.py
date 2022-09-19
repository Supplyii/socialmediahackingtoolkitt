import os

def command(comando):
	os.system(comando)

command("clear")


start = input("Welcome to setup, start setup? [y/n]\n: ")
if start == "y":
	pass
else:
	exit()
print("\n\nWINDSCRIBE VPN INSTALLATION\n\n")

command("apt-get update")
command("apt-get install windscribe-cli")
command('echo "\n||||||||||||||||||||||||||||||||\nNow login into your windscribe accoun, if you dont have one create it here: https://windscribe.com/login\n|||||||||||||||||||||||||||||||\n"')
command("windscribe login")
command("pip3 install instaloader")
