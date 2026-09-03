#modulo: str: Es un parámetro posicional obligatorio. Se utiliza .upper() para garantizar que siempre se formatee en mayúsculas.
#*mensajes: str (*args): Recibe una cantidad variable de argumentos no nombrados (posicionales) en forma de tupla. 
# Usamos enumerate(mensajes, start=1) para numerar cada línea secuencialmente a partir de [1].
def generar_auditoria_sistema(modulo: str, *mensajes: str, **metadatos) -> str:
    lineas = []

    
    # 1. Módulo en mayúsculas
    lineas.append(f"MÓDULO: {modulo.upper()}")
    
    # 2. Procesamiento y numeración de mensajes (*args)
    lineas.append("MENSAJES:")
    if mensajes:
        for i, mensaje in enumerate(mensajes, start=1):
            lineas.append(f"  [{i}] {mensaje}")
    else:
        lineas.append("  (Sin mensajes)")

    #**metadatos (**kwargs): Recibe una cantidad variable de argumentos nombrados (clave-valor) en forma de diccionario. 
    # Recorremos sus ítems convirtiendo la clave a mayúsculas y formateándola como CLAVE: VALOR.   
    # 3. Desglose de metadatos (**kwargs)
    lineas.append("METADATOS:")
    if metadatos:
        for clave, valor in metadatos.items():
            lineas.append(f"  {clave.upper()}: {valor}")
    else:
        lineas.append("  (Sin metadatos)")
        
    # Unión de todas las lineas en un reporte multi-linea
    return "\n".join(lineas)


# ==========================================
# PRUEBA REQUERIDA
# ==========================================
if __name__ == "__main__":
    log = generar_auditoria_sistema(
        "AUTH", 
        "Intento fallido", 
        "Bloqueo de IP", 
        usuario="admin", 
        ip="192.168.1.10"
    )
    
    print(log)