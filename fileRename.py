import os
import sys
import re
import sys
import platform
import datetime
import json


def path():
    confirm = input(
        '¿Están los archivos en la misma carpeta que el programa?: [s/n] ')
    ruta = os.getcwd()
    if confirm == "s" or confirm == "S":

        print("Buscando archivos en: " + ruta)
    elif confirm == "n" or confirm == "N":
        ruta = input('Introduce la ruta donde están los archivos: ')
        exist = os.path.exists(ruta)
        if exist == True:
            print("Buscando archivos en: " + ruta)
            return ruta
        else:
            error = "La ruta " + ruta + " no es válida"
            print("")
            print(error)
            return sys.exit()
    else:
        error = "Carácter " + ruta + " invalido"
        print(error)
        return sys.exit()


def archives(path):
    actual = input('Indicame lo que quieres sustituir (!): ')
    directorio = os.listdir(path)
    numero = 0
    directorios = []
    for archivo in directorio:
        if archivo.find(actual) != -1:
            numero += 1
            directorios.append(archivo)

    if numero > 0:
        print("He econtrado " + str(numero) + " archivos con la palabra " + actual)
        remplace = input('Cambiar ' + actual + ' por: ')
        confirm = input('¿Deseas cambiar ' + actual + ' por ' +
                        remplace + ' en ' + str(numero) + ' archivos? [s/n]: ')

        if confirm == "s" or confirm == "S":
            for archivo in directorios:
                modif = archivo.replace(actual, remplace)
                os.rename(archivo, modif)

            print("Se han cambiado los archivos correctamente")
        elif confirm == "n" or confirm == "N":
            cambio = []
            for archivo in directorios:
                modif = archivo.replace(actual, remplace)
                cambio.append(modif)

            consulta(directorios, cambio)

    else:

        error = "No he encontrado ningún archivo con la palabra " + actual
        print(error)
        return sys.exit()


def consulta(original, cambio):
    confirm = input("¿Deseas generar una consulta?  [s/n]: ")
    if confirm == "s" or confirm == "S":
        nOriginal = len(original)
        nCambio = len(cambio)
        if nOriginal == nCambio:
            numero = 0
            with open('consulta.txt', 'a') as f:
                for item in original:
                    f.write(item + " ==> " + cambio[numero] + "\n")
                    numero += 1
            ruta = os.getcwd()

            print('registro creado en ' + ruta)
    elif confirm == "n" or confirm == "N":
        return sys.exit()


print("  ___ _ _                                         _   __  ")
print(" | __(_) |___   _ _ ___ _ _  __ _ _ __  ___  __ _/ | /  \ ")
print(" | _|| | / -_) | '_/ -_) ' \/ _` | '  \/ -_) \ V / || () |")
print(" |_| |_|_\___| |_| \___|_||_\__,_|_|_|_\___|  \_/|_(_)__/ ")
print("                                          by  https://github.com/isaacJP  ")
print("")
try:
    ruta = path()
    archivos = archives(ruta)
except KeyboardInterrupt:
    print('')
    print('Cancelado por el usuario ctrl^c')
except SystemExit:
    print('')
except FileExistsError:
    print(sys.exc_info()[1])
    print("Todos los demás cambios se han realizado correctamente")
