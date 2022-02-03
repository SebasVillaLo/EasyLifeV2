#!/usr/bin/env python3
import subprocess
from collections import OrderedDict
import os
from os.path import exists
import urllib.request as request
from sys import argv

try:
    todosArchivos = []
    print("Bienvenido, espero sea se tu agrado mi primer script. :D\n")
    print("-----------------------------------------------------------------\n")
    print(
        "Asegurate de estar en la carpeta donde vas a crear la carpeta y los archivos")
    print("Ya sea el low leves o el higher level, o en la carpeta que gustes.")
    print("-----------------------------------------------------------------\n")
    path = input(
        "Ingrese a continuacion el nombre de la carpeta donde van todos los archivos (ejem: 0x15-python_hola): ").lower().strip("/")
    if exists(path) == False:
        subprocess.run(["mkdir", path])
    else:
        print('Este directorio ya existe, quieres que se cree uno vacio? (Si o No)')
        res = input("~ ")
        res.lower()
        if res == 'si':
            subprocess.run(["rm", "-rf", path])
            subprocess.run(["mkdir", path])
        elif (res == 'no'):
            print("Vale, trabajaremos con el que ya existe")
    print(path)
    print("-----------------------------------------------------------------\n")
    print("Ingrese el nombre de los archivos (por cada nombre presiona un enter, si ya terminaste, da enter)\n")
    print("Para eliminar el ultimo archivo ingresado, escriba 'del' ")
    print("Si pusiste un archivo repedito, no te preocupes que se elimina solito :3")
    print("\nsin el README, ese te lo hago yo :D\n")
    pathv2 = path + "/"
    readme = pathv2 + 'README.md'
    while True:
        archivos = input("~ ")
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
            print(f"El siguiente archivo ha sido eliminado {index}")
    comentario = input(
        "Quieres que tus archivos tengan el PATH? (#!/usr/bin/node): ")
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
    print("Graicas por usar mi Script :D\n")
    print("Todo se ha creado correctamente")
except KeyboardInterrupt:
    os.system("clear")
    print("Se cerro el script")
