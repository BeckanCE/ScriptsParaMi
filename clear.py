import os
import time

directorio = "/var/www/html/demos/files"  # Reemplaza esto con la ruta de tu directorio

# Obtener la fecha actual en segundos desde el epoch
tiempo_actual = time.time()

# Definir el límite de 3 días en segundos
limite_antiguedad = 3 * 24 * 60 * 60  # 3 días * 24 horas * 60 minutos * 60 segundos

# Recorrer los archivos en el directorio
for archivo in os.listdir(directorio):
    ruta_archivo = os.path.join(directorio, archivo)
    
    # Verificar si el elemento es un archivo
    if os.path.isfile(ruta_archivo):
        # Obtener la fecha de la última modificación del archivo en segundos desde el epoch
        tiempo_ultima_modificacion = os.path.getmtime(ruta_archivo)
        
        # Calcular la antigüedad del archivo
        antiguedad_archivo = tiempo_actual - tiempo_ultima_modificacion
        
        # Eliminar el archivo si es más antiguo que el límite
        if antiguedad_archivo > limite_antiguedad:
            os.remove(ruta_archivo)
            print(f"Archivo eliminado: {ruta_archivo}")
