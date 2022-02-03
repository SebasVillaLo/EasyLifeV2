#!/usr/bin/env python3
import subprocess
from collections import OrderedDict
import os
from os.path import exists
from colorama import init, Fore

try:
    init()
    todosArchivos = []
    print(Fore.BLUE+"Bienvenido, espero sea se tu agrado mi primer script. :D\n")
    print(Fore.YELLOW+"-----------------------------------------------------------------\n")
    print(Fore.BLUE+"Asegurate de estar en la carpeta donde vas a crear la carpeta y los archivos")
    print(Fore.BLUE+"Ya sea el low level, el higher level o en la carpeta que gustes.")
    print(Fore.YELLOW+"\n-----------------------------------------------------------------\n")
    print(Fore.RED+"Ingrese a continuacion el nombre de la carpeta donde van todos los archivos Ejem: (0x15-python_hola)")
    path = input(Fore.GREEN+"\n~ ").lower().strip("/")
    if exists(path) == False:
        subprocess.run(["mkdir", path])
    else:
        print(Fore.RED+'\nEste directorio ya existe, quieres que se cree uno vacio? (Si o No)\n')
        res = input(Fore.GREEN+"~ ")
        res.lower()
        if res == 'si':
            subprocess.run(["rm", "-rf", path])
            subprocess.run(["mkdir", path])
        elif (res == 'no'):
            print(Fore.BLUE+"\nVale, trabajaremos con el que ya existe")
    print(Fore.YELLOW+"-----------------------------------------------------------------\n")
    print(Fore.BLUE+"Ingrese el nombre de los archivos (por cada nombre presiona un enter, si ya terminaste, da enter)\n")
    print(Fore.MAGENTA+"Para eliminar el ultimo archivo ingresado, escriba 'del' ")
    print(Fore.MAGENTA+"Si pusiste un archivo repetido, no te preocupes que se elimina solito :3")
    print(Fore.RED+"\n -- El README te lo hago yo :D -- \n")
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
            print(Fore.MAGENTA+f"\nEl siguiente archivo ha sido eliminado {index}")
    print(Fore.YELLOW+"-----------------------------------------------------------------\n")
    print(Fore.MAGENTA+f"Quieres que tus archivos tengan el PATH? Ejem: (#!/usr/bin/node)")
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
    print(Fore.BLUE+"Graicas por usar mi Script :D\n")
    print(Fore.BLUE+"Todo se ha creado correctamente")
except KeyboardInterrupt:
    os.system("clear")
    print(Fore.BLUE+"Se cerro el script")
