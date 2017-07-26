#coding: utf-8

try:
    from time import *
    from random import *
    import os
    import glob
    import platform
except ImportError:
    print("Missing Modules in Python...")
    main = input("Press a [ENTER] for Continue...")
    exit()

version = platform.python_version()
print("Python Version: "+ version)


__version__ = "1.1.000-mixsys-00001"
__author__ = "Python Works"

# Repos raw
__git_raw__ = "https://github.com/Python-Library-Work/shell.git"


"""
try:
    checkfolder = open('./Users/.main.txt', 'r')
    checkfolder.read()
    checkfolder.close()
    print("[*] Users folders dectected !!!")
except:
    os.system("mkdir ./Users")
    checkfolder = open('./Users/.main.txt')
    checkfolder.close()
"""
def __init_shell__():
    print("[*] Shell Version: "+ __version__)
    sleep(1)
    print("[*] Support Version: null")

# In next system...

"""
try:
    cursor = open('cursor.conf', 'r')
    cursor1 = cursor.read()
    cursor.close()
    print("Cursor Defined is: "+ cursor1)
except:
"""
__init_shell__()

cursor1 = "shell-1.1.000~$: "
main2 = 1
while(main2<100):
	main = str(input("shell~#: "))
	# Processing Area
	if(main=="shutdown"):
		print("Shutdown...")
		sleep(1)
		break
		print("{*} Retriggering the SystemStart...")
	elif(main=="edit-cursors"):
		os.system("nano ./cursor.conf")
	elif(main=="support"):
		try:
			import support
		except:
			print("[*] Not Support of Mix System...")
	elif(main=="patch"):
		try:
			patch.backend()
		except:
			print("[*] Not patch of Mix System...")
	elif(main=="dectect-sys"):
		x = platform.system()
		z = platform.python_version()
		print("System: "+ x)
		print("Py Version: "+ z)
	elif(main=="edit"):
		main23 = input("Archive: ")
		os.system("nano ./Users/"+ main23)
	elif(main=="dir"):
		os.system("ls ./Users/")
	elif(main=="del"):
		main21 = input("Del?: ")
		os.system("rm -rf ./Users/"+ main21)
	elif(main=="clear-cache"):
		try:
			os.system("rm -rf ./__pycache__/")
			print("Cache cleared")
		except:
			print("Error in cache...")
	elif(main=="exec"):
		main231 = input("Exec: ")
		os.system("python ./Users/"+ main231)
	elif(main=="update-shell"):
		print("Trying Updating Shell")
		os.system("chmod 777 ./updater.run")
		os.system("./updater-run")
	elif(main==""):
		pass
	else:
		pass

print("Closing a Sys !!! bye bye")




