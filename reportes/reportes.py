def generar_reporte(datos):
    return f"Reporte con {len(datos)} registros"
def exportar_reporte(reporte, ruta):
    with open(ruta, "w") as archivo:
        archivo.write(reporte)
