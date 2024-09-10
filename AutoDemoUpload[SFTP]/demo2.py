import os
import pysftp
import time
import discord
from discord_webhook import DiscordWebhook

# Configuración de la carpeta local y las credenciales SFTP
LOCAL_FOLDER = '/home/steam/Steam/steamapps/common/l4d2/left4dead2/demos'
REMOTE_FOLDER = '/var/www/html/demos/files'
HOST = '161.132.49.131'
USERNAME = 'root'
PASSWORD = 'cAs4ndra'

# Función para subir archivo a través de SFTP
def upload_file(local_path, remote_path):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    
    with pysftp.Connection(HOST, username=USERNAME, password=PASSWORD, cnopts=cnopts) as sftp:
        sftp.put(local_path, remote_path)

# Función para enviar mensaje a través de Discord Webhook
def send_discord_message(file_name, file_size_mb, map_name):
    webhook_url = 'https://discord.com/api/webhooks/1234676937071525889/TLbNncL7k9M75iWbBgTAr0u9qg53t_dOgmNBiKc3bnNqK4ONj6vTjEvNp_ik5VrliAkC'
    webhook = DiscordWebhook(url=webhook_url, content='--------------------------\n    🎥 SourceTV 📺   \n--------------------------\n   **Nueva demostración**   \n--------------------------\n* Peso: {:.2f} MB\n* Mapa: {}\n* Link: https://makako.xyz/demos/files/{}'.format(file_size_mb, map_name, file_name))
    response = webhook.execute()

# Función principal
def main():
    # Lista todos los archivos en la carpeta local
    files = os.listdir(LOCAL_FOLDER)

    if not files:
        print("No hay archivos en la carpeta local.")
        return

    # Recorre cada archivo
    for file_name in files:
        file_path = os.path.join(LOCAL_FOLDER, file_name)
        
        # Verifica si el archivo fue modificado hace más de 7 minutos
        if time.time() - os.path.getmtime(file_path) > 7 * 60:
            try:
                # Sube el archivo al servidor remoto
                remote_path = os.path.join(REMOTE_FOLDER, file_name)
                upload_file(file_path, remote_path)
                
                # Extrae información del archivo para el mensaje de Discord
                file_size_bytes = os.path.getsize(file_path)
                file_size_mb = file_size_bytes / (1024 * 1024)  # Convertir a megabytes
                map_name = file_name.split('-')[-1].split('.')[0]
                
                # Envía el mensaje a Discord
                send_discord_message(file_name, file_size_mb, map_name)
                
                # Si la subida es exitosa, elimina el archivo local
                os.remove(file_path)
                
                print(f"El archivo '{file_name}' se ha subido correctamente.")
            except Exception as e:
                print(f"No se pudo subir el archivo '{file_name}': {str(e)}")
        else:
            print(f"El archivo '{file_name}' no cumple con el tiempo mínimo.")

if __name__ == "__main__":
    main()
