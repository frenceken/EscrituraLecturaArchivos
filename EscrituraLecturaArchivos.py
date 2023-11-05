"""Archivos CSV en python"""
import csv  # sirve para almacenar datos tabulares, como por ejemplo hojas de calculos
import pandas as pd  # tambien funciona para almacenar datos tabulares
import json
import pickle  # se puede usar para guardar en forma de archivos binarios
from PIL import Image  # se usa para abrir y trabajar imagenes

#---------------------------------------------------ARCHIVOS .csv-------------------------------------------------------------
escritura_datos_csv = [["\nNombre, Apellido, edad, Email"],
                           ["Ronald", "Frenzel", 42, "email@gmail.com"],
                           ["Joseline", "Sequera", 40, "email@yahoo.com"]]
    
escritura_pandas = {"Nombres": ["Ronald", "Joseline", "Leonardo", "Giselle"],  
                        "Edad": [42, 40, 13, 3],
                        }  # esta estructura de datos es IMPORTANTE que tengan la misma longitud (misma cantidad de elementos)

escritura_txt = ["Brais", "Niko", "Juan"]

escritura_json = {"Nombre": "Ramon",
                       "Apellido": "Dalto",
                       "Edad": 42,
                       "Email": "unemail@gmail.com"}  # se crea una estructura de datos antes de crear el archivo .json

try:
#-------------------------------------------------ARCHIVOS .CSV---------------------------------------------------------------    
    archivo_panda = pd.DataFrame(escritura_pandas) # estructura de datos pandas que se asemeja a una tabla.
    archivo_panda.to_csv("Clases con Dalto de Soy Dalto/lectura de datos csv/listado de nombres2.csv", index=False)  # "index=False" se usa para evitar que panda agrege una columna adicional.

    with open("Clases con Dalto de Soy Dalto/lectura de datos csv/listado de nombres2.csv", "r", encoding="UTF-8") as archivo_pd:  # hecho con pandas.
        print(pd.read_csv(archivo_pd))  # con pandas de debe indicar el tipo de archivo de datos tabulares en este caso es csv.


    with open("Clases con Dalto de Soy Dalto/lectura de datos csv/listado de nombres.csv", mode="a", newline="") as archivo_csv:  # hecho con biblioteca CSV.
        escritura_csv = csv.writer(archivo_csv)  # mode= para indicar el mode de escritura, newline="" para evitar saltos de linea en diferentes sistemas operativos.
        for fila in escritura_datos_csv:  # se realiza un for en la variable con los datos.
            escritura_csv.writerow(fila)  # el archivo se escribira con cada linea del for.
    
    with open("Clases con Dalto de Soy Dalto/lectura de datos csv/listado de nombres.csv", "r", encoding="UTF-8") as archivo_csv:
        datos_csv = csv.reader(archivo_csv)
        for fila in datos_csv:
            print(fila)        
    
#--------------------------------------------------ARCHIVOS .xlsx-------------------------------------------------------------    
    archivo_xlsx = pd.DataFrame(escritura_pandas)
    archivo_xlsx.to_excel("Clases con Dalto de Soy Dalto/lectura de datos csv/archivo.xlsx", index=False)
    
    
    archivo_xlsx = "Clases con Dalto de Soy Dalto/lectura de datos csv/archivo.xlsx"
    datos_xlsx = pd.read_excel(archivo_xlsx)  # se usa sheet_name="nombreDeLaHoja" se usa para leer una hoja en concreto, por defecto Pandas leera la Hoja1 
    print(datos_xlsx)

#-------------------------------------------------ARCHIVOS .txt---------------------------------------------------------------
    with open("Clases con Dalto de Soy Dalto/lectura de datos csv/lista.txt", "w", encoding="UTF-8") as archivo_txt:
        archivo_txt.write(str(escritura_txt))  # IMPORTANTE se debe pasar los datos a string crea el archivo vacio y el programa da error

    
    with open("Clases con Dalto de Soy Dalto/lectura de datos csv/lista.txt", "r", encoding="UTF-8") as archivo_txt:
        lectura_txt = archivo_txt.read()
        print(lectura_txt)
    
#-------------------------------------------------ARCHIVOS .json--------------------------------------------------------------
    with open("Clases con Dalto de Soy Dalto/lectura de datos csv/archivo.json", "w", encoding="UTF-8") as archivo_json:
        json.dump(escritura_json, archivo_json)  # se importa biblioteca json y se usa funcion dump para crear archivos, dumps para escribir directamente en un archivo
# escritura_json se guarda en archivo_json

    with open("Clases con Dalto de Soy Dalto/lectura de datos csv/archivo.json", "r", encoding="UTF-8") as archivo_json:
        lectura_json = archivo_json.read()
        print(lectura_json)

#-------------------------------------------------ARCHIVOS EN BINARIO---------------------------------------------------------
    with open("Clases con Dalto de Soy Dalto/lectura de datos csv/archivo1.bin", "wb") as archivo_bin:
        datos_bin = b"\x48\x65\x6c\x6c\x6f"
        archivo_bin.write(datos_bin)

    with open("Clases con Dalto de Soy Dalto/lectura de datos csv/archivo1.bin", "rb") as archivo_bin:
        lectura_bin = archivo_bin.read()
        print(lectura_bin)

    with open("Clases con Dalto de Soy Dalto/lectura de datos csv/archivo2.pkl", "wb") as archivo_bin:
        pickle.dump(escritura_txt, archivo_bin)

    with open("Clases con Dalto de Soy Dalto/lectura de datos csv/archivo2.pkl", "rb") as archivo_bin:
        lectura2_bin = pickle.load(archivo_bin)
        print(lectura2_bin) 

#--------------------------------------------------ARCHIVOS DE IMAGEN BMP,GIF,JPG,TIF,PNG Y MAS--------------------------------
    imagen = Image.open("Clases con Dalto de Soy Dalto\lectura de datos csv/2011-Jeep-Wrangler-Interior.jpg")
    imagen.show()

    imagen2 = Image.open("Clases con Dalto de Soy Dalto\lectura de datos csv/mitsubischi outlander 2003 4x4 fato 2.png")
    imagen2.show()
    
    
except FileNotFoundError:
    print("EL archivo no se puede encontrar")
