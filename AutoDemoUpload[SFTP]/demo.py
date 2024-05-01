import os
import time
import paramiko
import requests
import datetime

# Configuración para la conexión SFTP
HOST = 'ipdelhost'
PUERTO = 22
USUARIO = 'usuario'
CONTRASEÑA = 'contraseña'
RUTA_REMOTA = 'donde/se/suben/los/archivos'

# Configuración del Discord Webhook
DISCORD_WEBHOOK_URL = 'tu_url_webhook_discord'

def enviar_mensaje_discord(nombre_archivo):
    mensaje = f"----------------------\n        SourceTV\n----------------------\n\n1.- Si quieres ver tus partidas para revivirla o sospechas de un usuario por uso de hacks puedes encontrar tus partidas grabadas en: \n\n(*) https://tudominio.com/ruta/demos\n\n2.- Descarga la última partida jugada a través del siguiente enlace\n\n(*) https://link/del/demo/{nombre_archivo}"
    data = {'content': mensaje}
    requests.post(DISCORD_WEBHOOK_URL, json=data)

def subir_archivo_sftp(local_path, remote_path):
    try:
        transport = paramiko.Transport((HOST, PUERTO))
        transport.connect(username=USUARIO, password=CONTRASEÑA)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(local_path, remote_path)
        sftp.close()
        transport.close()
        return True
    except Exception as e:
        print(f"Error al subir archivo por SFTP: {e}")
        return False

def eliminar_archivo(local_path):
    try:
        os.remove(local_path)
        print(f"Archivo {local_path} eliminado correctamente.")
    except Exception as e:
        print(f"No se pudo eliminar el archivo {local_path}: {e}")

def main():
    carpeta = 'ruta/donde/sourcetv/graba/los/demos'
    archivos = os.listdir(carpeta)
    
    for archivo in archivos:
        ruta_completa = os.path.join(carpeta, archivo)
        ultima_modificacion = os.path.getmtime(ruta_completa)
        tiempo_actual = time.time()
        diferencia_tiempo = tiempo_actual - ultima_modificacion
        diferencia_minutos = diferencia_tiempo / 60

        if diferencia_minutos >= 6:
            if subir_archivo_sftp(ruta_completa, os.path.join(RUTA_REMOTA, archivo)):
                enviar_mensaje_discord(archivo)
                eliminar_archivo(ruta_completa)
        else:
            print(f"El archivo {archivo} no cumple con el tiempo mínimo de modificación para ser subido.")

if __name__ == "__main__":
    main()
