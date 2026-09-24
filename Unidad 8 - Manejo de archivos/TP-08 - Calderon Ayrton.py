#Ejercicio 1 
#1.Guardo datos en la lista
#================================
productos = [
    "Lapicera,150.5,10\n"
    "Regla,100.0,15\n"
    "Cuaderno,300,30\n"
]

#Creo un archivo .txt
with open("productos.txt", "w") as archivo:
    archivo.writelines(productos)