import subprocess

def ejecutar_comandos():
    comandos = [
        "ls",
        "pwd",
        "echo 'Hola Mundo'",
        /etc/init.d/srcds1 restart
        /etc/init.d/srcds2 restart
        /etc/init.d/srcds3 restart
        /etc/init.d/srcds4 restart
        /etc/init.d/srcds5 restart
        /etc/init.d/srcds6 restart
        /etc/init.d/srcds7 restart
        /etc/init.d/srcds8 restart
        /etc/init.d/srcds9 restart
        /etc/init.d/srcds10 restart
        /etc/init.d/srcds11 restart
        /etc/init.d/srcds12 restart
        /etc/init.d/srcds13 restart
        /etc/init.d/srcds14 restart
        /etc/init.d/srcds15 restart
    ]

    for comando in comandos:
        print(f"Ejecutando comando: {comando}")
        try:
            resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
            print("Salida estándar:")
            print(resultado.stdout)
            print("Salida de error:")
            print(resultado.stderr)
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el comando {comando}: {e}")

if __name__ == "__main__":
    ejecutar_comandos()
