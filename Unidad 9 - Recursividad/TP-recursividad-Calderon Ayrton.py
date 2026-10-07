# ==============================================================================
# TRABAJO PRACTICO: ANALISIS Y NAVEGACION DE SISTEMAS DE ARCHIVOS (RECURSIVIDAD)
# ==============================================================================


# ------------------------------------------------------------------------------
# 2. ESTRUCTURA DE DATOS BASE
# ------------------------------------------------------------------------------

class Archivo:
    """Clase que representa un archivo individual dentro del sistema."""

    def __init__(self, nombre: str, tamaño_bytes: int):
        self.nombre = nombre
        self.tamaño_bytes = tamaño_bytes


class Directorio:
    """Clase que representa un directorio/carpeta."""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.archivos = []
        self.subdirectorios = []


# ------------------------------------------------------------------------------
# 3. FUNCIONES RECURSIVAS
# ------------------------------------------------------------------------------


# --- FUNCION PARA MOSTRAR LA ESTRUCTURA EN FORMA DE ARBOL ---
def mostrar_arbol(directorio: Directorio, nivel: int = 0):
    prefijo = "  " * nivel
    print(f"{prefijo}├── {directorio.nombre}/")

    for archivo in directorio.archivos:
        print(f"{prefijo}  ├── {archivo.nombre} ({archivo.tamaño_bytes} bytes)")

    for subdirectorio in directorio.subdirectorios:
        mostrar_arbol(subdirectorio, nivel + 1)


# --- FUNCION 1: Calculo del Tamaño Total de un Directorio ---
def calcular_tamaño_total(directorio: Directorio) -> int:
    tamaño_archivos_locales = sum(
        archivo.tamaño_bytes for archivo in directorio.archivos
    )

    tamaño_subdirectorios = 0
    for subdirectorio in directorio.subdirectorios:
        tamaño_subdirectorios += calcular_tamaño_total(subdirectorio)

    return tamaño_archivos_locales + tamaño_subdirectorios


# --- FUNCION 2: Busqueda de Archivo por Extension ---
def buscar_por_extension(
    directorio: Directorio, extension: str, ruta_actual: str = ""
) -> list[str]:
    if not ruta_actual:
        ruta_actual = directorio.nombre
    else:
        ruta_actual = f"{ruta_actual}/{directorio.nombre}"

    resultados = []

    for archivo in directorio.archivos:
        if archivo.nombre.endswith(extension):
            resultados.append(f"{ruta_actual}/{archivo.nombre}")

    for subdirectorio in directorio.subdirectorios:
        resultados.extend(
            buscar_por_extension(subdirectorio, extension, ruta_actual)
        )

    return resultados


# --- FUNCION 3: Eliminacion Recursiva de Archivos Vacios ---
def limpiar_archivos_vacios(directorio: Directorio) -> int:
    eliminados_locales = sum(
        1 for archivo in directorio.archivos if archivo.tamaño_bytes == 0
    )

    directorio.archivos = [
        archivo
        for archivo in directorio.archivos
        if archivo.tamaño_bytes > 0
    ]

    eliminados_subdirectorios = 0
    for subdirectorio in directorio.subdirectorios:
        eliminados_subdirectorios += limpiar_archivos_vacios(subdirectorio)

    return eliminados_locales + eliminados_subdirectorios


# ------------------------------------------------------------------------------
# 4. EJERCICIO INTEGRADOR Y CASO DE PRUEBA
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # 1. Creacion del directorio raiz "root"
    root = Directorio("root")
    root.archivos.append(Archivo("documento.pdf", 1500))
    root.archivos.append(Archivo("config.txt", 0))

    # 2. Subdirectorio "imagenes"
    imagenes = Directorio("imagenes")
    imagenes.archivos.append(Archivo("foto1.png", 2000))
    imagenes.archivos.append(Archivo("foto2.png", 3500))
    root.subdirectorios.append(imagenes)

    # 3. Subdirectorio "proyectos" y "temp"
    proyectos = Directorio("proyectos")
    proyectos.archivos.append(Archivo("avance.pdf", 800))

    temp = Directorio("temp")
    temp.archivos.append(Archivo("log.txt", 0))
    proyectos.subdirectorios.append(temp)

    root.subdirectorios.append(proyectos)

    root.archivos.append(Archivo("test.pdf", 10000))
        
    # --------------------------------------------------------------------------
    # EJECUCION Y SALIDAS
    # --------------------------------------------------------------------------
    print("==================================================")
    print("           ESTRUCTURA VISUAL DEL ARBOL            ")
    print("==================================================")
    mostrar_arbol(root)

    print("\n==================================================")
    print("        RESULTADOS DE VALIDACION DEL TP           ")
    print("==================================================")

    # Validacion 1
    tamaño_total = calcular_tamaño_total(root)
    print(f"1. Tamaño total del directorio root: {tamaño_total} bytes")

    # Validacion 2
    archivos_pdf = buscar_por_extension(root, ".pdf")
    print(f"2. Archivos con extension '.pdf' encontrados:")
    for ruta in archivos_pdf:
        print(f"   - {ruta}")

    # Validacion 3
    borrados = limpiar_archivos_vacios(root)
    print(f"3. Archivos vacios (0 bytes) eliminados: {borrados}")

    # Arbol despues de la limpieza
    print("\n==================================================")
    print("        ESTRUCTURA TRAS LA LIMPIEZA               ")
    print("==================================================")
    mostrar_arbol(root)