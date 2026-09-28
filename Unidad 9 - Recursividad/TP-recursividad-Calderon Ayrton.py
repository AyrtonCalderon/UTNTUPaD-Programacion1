# ==============================================================================
# TRABAJO PRACTICO: ANALISIS Y NAVEGACION DE SISTEMAS DE ARCHIVOS (RECURSIVIDAD)
# ==============================================================================


# ------------------------------------------------------------------------------
# 2. ESTRUCTURA DE DATOS BASE
# ------------------------------------------------------------------------------

class Archivo:
    """Clase que representa un archivo individual dentro del sistema.

    Es un elemento hoja (no contiene otros objetos dentro).
    """

    def __init__(self, nombre: str, tamaño_bytes: int):
        self.nombre = nombre  # Nombre del archivo (ej. 'documento.pdf')
        self.tamaño_bytes = tamaño_bytes  # Tamaño en bytes (ej. 1500)


class Directorio:
    """Clase que representa un directorio/carpeta.

    Es una estructura de nodo jerarquica que puede contener tanto archivos
    locales como otros subdirectorios de forma autorreferencial.
    """

    def __init__(self, nombre: str):
        self.nombre = nombre  # Nombre del directorio (ej. 'root')
        self.archivos = []  # Lista que contendra objetos de clase Archivo
        self.subdirectorios = (
            []
        )  # Lista que contendra objetos de clase Directorio


# ------------------------------------------------------------------------------
# 3. FUNCIONES RECURSIVAS REQUERIDAS
# ------------------------------------------------------------------------------


# --- FUNCION 1: Calculo del Tamaño Total de un Directorio ---
def calcular_tamaño_total(directorio: Directorio) -> int:
    """Calcula recursivamente el peso total de un directorio sumando sus archivos

    locales y el peso de todas sus subcarpetas.
    """
    # CASO BASE: Sumar el tamaño de los archivos que estan directamente en esta carpeta
    tamaño_archivos_locales = sum(
        archivo.tamaño_bytes for archivo in directorio.archivos
    )

    # PASO RECURSIVO: Recorrer cada subdirectorio y llamar recursivamente a la funcion
    tamaño_subdirectorios = 0
    for subdirectorio in directorio.subdirectorios:
        # La llamada recursiva calcula el peso total de la subcarpeta completa
        tamaño_subdirectorios += calcular_tamaño_total(subdirectorio)

    # El resultado final es la combinacion del peso local mas el peso de los subdirectorios
    return tamaño_archivos_locales + tamaño_subdirectorios


# --- FUNCION 2: Busqueda de Archivo por Extension ---
def buscar_por_extension(
    directorio: Directorio, extension: str, ruta_actual: str = ""
) -> list[str]:
    """Recorre la jerarquia de directorios y devuelve una lista con las rutas

    completas de los archivos que coincidan con la extension buscada (ej.
    '.pdf').
    """
    # Construccion de la ruta jerarquica acumulada (ej. 'root/proyectos')
    if not ruta_actual:
        ruta_actual = directorio.nombre  # Si es el directorio raiz inicial
    else:
        ruta_actual = f"{ruta_actual}/{directorio.nombre}"  # Anexa el nombre de la subcarpeta

    resultados = []

    # INSPECCION LOCAL: Revisa los archivos del directorio actual
    for archivo in directorio.archivos:
        # endswith verifica si el nombre termina con la extension indicada
        if archivo.nombre.endswith(extension):
            resultados.append(f"{ruta_actual}/{archivo.nombre}")

    # PASO RECURSIVO: Llama a la funcion para cada subdirectorio e integra los resultados
    for subdirectorio in directorio.subdirectorios:
        # .extend une la lista devuelta por la llamada recursiva a la lista de resultados actual
        resultados.extend(
            buscar_por_extension(subdirectorio, extension, ruta_actual)
        )

    return resultados


# --- FUNCION 3: Eliminacion Recursiva de Archivos Vacios (Limpieza de Disco) ---
def limpiar_archivos_vacios(directorio: Directorio) -> int:
    """Elimina recursivamente todos los objetos Archivo cuyo tamaño sea 0 bytes y

    retorna el numero total de archivos eliminados en toda la jerarquia.
    """
    # 1. Contar cuantos archivos vacios (0 bytes) existen en la carpeta actual
    eliminados_locales = sum(
        1 for archivo in directorio.archivos if archivo.tamaño_bytes == 0
    )

    # 2. Filtrar la lista del directorio actual, conservando solo los que pesan mas de 0 bytes
    directorio.archivos = [
        archivo
        for archivo in directorio.archivos
        if archivo.tamaño_bytes > 0
    ]

    # 3. PASO RECURSIVO: Propagar el proceso de limpieza sobre cada subdirectorio
    eliminados_subdirectorios = 0
    for subdirectorio in directorio.subdirectorios:
        # Acumula las eliminaciones realizadas en los niveles inferiores de la jerarquia
        eliminados_subdirectorios += limpiar_archivos_vacios(subdirectorio)

    # Devuelve la suma de las eliminaciones hechas localmente mas las de los subdirectorios
    return eliminados_locales + eliminados_subdirectorios


# ------------------------------------------------------------------------------
# 4. EJERCICIO INTEGRADOR Y CASO DE PRUEBA
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # 1. Creacion del directorio raiz "root"
    root = Directorio("root")
    root.archivos.append(Archivo("documento.pdf", 1500))  # Archivo de 1500 bytes
    root.archivos.append(Archivo("config.txt", 0))  # Archivo vacio (0 bytes)

    # 2. Creacion del subdirectorio "imagenes" y sus archivos
    imagenes = Directorio("imagenes")
    imagenes.archivos.append(Archivo("foto1.png", 2000))
    imagenes.archivos.append(Archivo("foto2.png", 3500))
    root.subdirectorios.append(imagenes)  # Se agrega "imagenes" dentro de "root"

    # 3. Creacion del subdirectorio "proyectos" y su subcarpeta "temp"
    proyectos = Directorio("proyectos")
    proyectos.archivos.append(Archivo("avance.pdf", 800))

    temp = Directorio("temp")
    temp.archivos.append(Archivo("log.txt", 0))  # Archivo vacio (0 bytes)
    proyectos.subdirectorios.append(
        temp
    )  # Se agrega "temp" dentro de "proyectos"

    root.subdirectorios.append(
        proyectos
    )  # Se agrega "proyectos" dentro de "root"

    # --------------------------------------------------------------------------
    # IMPRESION Y VALIDACION DE RESULTADOS EN CONSOLA
    # --------------------------------------------------------------------------
    print("==================================================")
    print("        RESULTADOS DE VALIDACION DEL TP           ")
    print("==================================================")

    # Validacion 1: Calculo del tamaño total (Esperado: 7800 bytes)
    tamaño_total = calcular_tamaño_total(root)
    print(f"1. Tamaño total del directorio root: {tamaño_total} bytes")

    # Validacion 2: Busqueda de archivos .pdf (Esperado: ['root/documento.pdf', 'root/proyectos/avance.pdf'])
    archivos_pdf = buscar_por_extension(root, ".pdf")
    print(f"2. Archivos con extension '.pdf' encontrados:")
    for ruta in archivos_pdf:
        print(f"   - {ruta}")

    # Validacion 3: Limpieza de archivos de 0 bytes (Esperado: 2 eliminados)
    borrados = limpiar_archivos_vacios(root)
    print(f"3. Archivos vacios (0 bytes) eliminados: {borrados}")

    # Comprobacion posterior: Verificamos el nuevo tamaño tras la limpieza
    nuevo_tamaño = calcular_tamaño_total(root)
    print(f"   -> Tamaño total tras la limpieza: {nuevo_tamaño} bytes")
    print("==================================================")