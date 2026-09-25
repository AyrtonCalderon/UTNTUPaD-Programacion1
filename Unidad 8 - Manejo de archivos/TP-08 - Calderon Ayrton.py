#Ejercicio 1 
#1.Guardo datos en la lista
#================================
productos = [
    "Lapicera,150.5,10\n"
    "Regla,100.0,15\n"
    "Cuaderno,300,30\n"
]

#Creo un archivo .txt
with open("Unidad 8 - Manejo de archivos/productos.txt", "w") as archivo:
    archivo.writelines(productos)
#====================================================
#Ejercicio 2
with open("Unidad 8 - Manejo de archivos/productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        print(partes)
        #Formatear salida 
        print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Unidades: {partes[2]}")
#==============================================================================================
#Ejercicio 3
#Agregar productos desde teclado

nombre = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio: ")
unidad = input("Ingrese la cantidad: ")

#Ingresar los datos para guardarlos en el archivo

nuevo_producto = f"{nombre},{precio},{unidad}\n"

#Guardar los datos ingresados
with open("Unidad 8 - Manejo de archivos/productos.txt", "a") as archivo:
    archivo.write(nuevo_producto)
#================================================================================
#4. Cargar productos en una lista de diccionarios: 
productos = []

#Leer el archivo línea por línea
with open("Unidad 8 - Manejo de archivos/productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
    
        #Armar el diccionario por cada producto
        producto= {
        "nombre": partes[0],
        "precio": float(partes[1]), #convierto el precio a numero decimal
        "cantidad": int(partes[2]) #La cantidad la pasamos a numero entero
        }

        #Guardamos el diccionario en la lista
        productos.append(producto)

#Imprimimos los produtos
print(productos)

#===========================================================================================
#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto.
#  Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.

#Escribir el nombre del producto a buscar
busqueda= input("Ingrese el nombre del producto a buscar: ")

#Bandera
encontrado = False

#Recorro la lista productos con un for
for product in productos:
    if product["nombre"].lower() == busqueda.lower():
        print(f"Producto encontrado:{product[nombre]} | Precio: ${product[precio]} | Cantidad: {product["Cantidad"]}") 
        encontrado = True
        break

#Mensaje por si no existe
if not encontrado:
    print("Error: El producto no existe en la lista") 
#====================================================================================================================================
#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.

with open("Unidad 8 - Manejo de archivos/productos.txt", "w") as archivo:

#Recorro la lista productos

    for product in productos:
        linea = f"{product['nombre']},{product['precio']},{product['cantidad']}\n"
        archivo.write(linea)

print("Archivo producto.txt actualizado")