import json
import time
import os
import datetime 

def actualizar_json(ruta_archivo, nuevo_parametro):
    """Actualiza el archivo JSON con el nuevo parámetro."""
    try:
        datetime.datetime.now()
        fecha_hora_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formato: YYYY-MM-DD HH:MM
        print(f"Fecha de inicio: {fecha_hora_str}")
        with open(ruta_archivo, 'r') as archivo:
            datos = json.load(archivo)

        # Modifica el parámetro que necesites
        datos['configuracion']['urlBaseDatos'] = nuevo_parametro  # Ejemplo: actualizar urlBaseDatos

        with open(ruta_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

        print(f"Archivo JSON actualizado con: {nuevo_parametro} a las {fecha_hora_str}")
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en {ruta_archivo}")
    except json.JSONDecodeError:
        print(f"Error: Archivo JSON inválido en {ruta_archivo}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    ruta_archivo = r"/var/jenkins_home/assets/configuracion.json"  # Reemplaza con tu ruta real
    nombre_archivo_log = "registro_actualizaciones.txt"

    # Lista de posibles parámetros (URLs, valores, etc.)
    parametros = [
        "./assets/20250601_2000_COMPUTOS.zip",
        "./assets/20250601_2005_COMPUTOS.zip",
        "./assets/20250601_2010_COMPUTOS.zip",
        # ... más parámetros
    ]

    indice_parametro = 0  # Índice para recorrer la lista de parámetros

    # Bucle while que se ejecuta mientras haya parámetros disponibles
    while indice_parametro < len(parametros):
        nuevo_parametro = parametros[indice_parametro]
        actualizar_json(ruta_archivo, nuevo_parametro)

        # Obtiene la fecha y hora actual
        ahora = datetime.datetime.now()
        fecha_hora_str = ahora.strftime("%Y-%m-%d %H:%M:%S") 
        # Escribe la fecha y hora en el archivo de registro
        with open(nombre_archivo_log, "a") as archivo_log:  # Abre el archivo en modo "append" (añadir)
            archivo_log.write(f"Actualización realizada el: {fecha_hora_str} con el parametro: {nuevo_parametro}\n")  # Agrega un salto de línea

        indice_parametro += 1  # Avanzar al siguiente parámetro

        if indice_parametro < len(parametros):  # Esperar solo si hay más parámetros
            time.sleep(300)  # Esperar 300 segundos (5 minutos)

    print("Se han utilizado todos los parámetros. El script ha terminado.")