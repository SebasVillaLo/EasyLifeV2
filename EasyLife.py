#!/usr/bin/env python3
import subprocess
from collections import OrderedDict
import os
from os.path import exists
from colorama import init, Fore

try:
    init()
    todosArchivos = []
    print(Fore.BLUE+"Welcome, I hope you like my first script. :D\n")
    print(Fore.YELLOW+"-----------------------------------------------------------------\n")
    print(Fore.BLUE+"Make sure you are in the folder where you are going to create the folder and files.")
    print(Fore.BLUE+"Either the low level, the higher level or in the folder of your choice.")
    print(Fore.YELLOW+"\n-----------------------------------------------------------------\n")
    print(Fore.RED+"Enter below the name of the folder where all the files go Ex: (0x15-python_hello)")
    path = input(Fore.GREEN+"\n~ ").lower().strip("/")
    if exists(path) == False:
        subprocess.run(["mkdir", path])
    else:
        print(Fore.RED+'\nThis directory already exists, do you want an empty directory to be created? (Yes or No)\n')
        res = input(Fore.GREEN+"~ ")
        res.lower()
        if res == 'si':
            subprocess.run(["rm", "-rf", path])
            subprocess.run(["mkdir", path])
        elif (res == 'no'):
            print(Fore.BLUE+"\nOkay, we will work with the existing one")
    print(Fore.YELLOW+"-----------------------------------------------------------------\n")
    print(Fore.BLUE+"Enter the name of the files (for each name press enter, if you are done, press enter).\n")
    print(Fore.MAGENTA+"To delete the last file entered, type 'del'. ")
    print(Fore.MAGENTA+"If you put a repeated file, don't worry, it will delete itself :3")
    print(Fore.RED+"\n -- The README I do it for you :D -- \n")
    pathv2 = path + "/"
    readme = pathv2 + 'README.md'
    while True:
        archivos = input(Fore.GREEN+"~ ")
        archivos.lower()
        if (len(archivos) > 0 and archivos != 'del'):
            todosArchivos.append(archivos.replace(" ", "_"))
        elif (archivos == ''):
            final = list(OrderedDict.fromkeys(todosArchivos))
            todosArchivos = final
            break
        else:
            index = todosArchivos[-1]
            todosArchivos.remove(index)
            print(Fore.MAGENTA+f"\nThe following file has been deleted {index}")
    print(Fore.YELLOW+"-----------------------------------------------------------------\n")
    print(Fore.MAGENTA+f"Do you want your files to have the PATH? Exem: (#!/usr/bin/node)")
    comentario = input(Fore.GREEN+"\n~ ")
    for i in range(len(todosArchivos)):
        if len(comentario) > 0:
            with open(f'{pathv2}{todosArchivos[i]}', 'w') as f:
                f.write(comentario)
            subprocess.run(["chmod", "a+x", f"{pathv2}{todosArchivos[i]}"])
        else:
            subprocess.run(["touch", f"{pathv2}{todosArchivos[i]}"])
            subprocess.run(["chmod", "a+x", f"{pathv2}{todosArchivos[i]}"])
    subprocess.run(["touch", f"{readme}"])
    f = open(readme, 'w')
    f.write(path)
    f.close()
    os.system('clear')
    print(Fore.BLUE+"Thanks for using my script :D\n")
    print(Fore.BLUE+"Everything has been created correctly")
except KeyboardInterrupt:
    os.system("clear")
    print(Fore.BLUE+"Script closed")
