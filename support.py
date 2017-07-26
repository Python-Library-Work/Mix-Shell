#coding: utf-8

import os
from time import *
from random import *

# Support is only for Mix System
# No disponible to Raw Versions

# Version
__version__ = "1.0.000-mixsys-support"

# Init dummy...
def init():
	print("Shell loaded... Support área")

main = 1
while(main<100):
	cursor = input("support@: ")
	if(cursor=="backup-make"):
		os.system("rm -rf ./backup.tar.gz")
		os.system("tar -cvzf backup.tar.gz ./* ")
		print("Backup Made with Sucess !!!")
	elif(cursor=="recovery-sys"):
		os.system("tar -xzvf ./backup.tar.gz ./")
		print("Recovered System in backup...")
	elif(cursor=="version-support"):
		print("Version: "+ __version__)
	elif(cursor=="exit"):
		print("ended shell")
		break
	elif(cursor=="get-raw-version"):
		try:
			os.system("git clone https://github.com/Python-Library-Work/shell.git")
		except:
			print("Verify or git is installed, or connection...")
	else:
		print("No command disponible: "+ cursor)



print("Support End")
