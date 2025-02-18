import json
import time
import os

def actualizar_json(ruta_archivo, nuevo_parametro):
    """Actualiza el archivo JSON con el nuevo parámetro."""
    try:
        with open(ruta_archivo, 'r') as archivo:
            datos = json.load(archivo)

        # Modifica el parámetro que necesites
        datos['configuracion']['urlBaseDatos'] = nuevo_parametro  # Ejemplo: actualizar urlBaseDatos

        with open(ruta_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

        print(f"Archivo JSON actualizado con: {nuevo_parametro}")
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en {ruta_archivo}")
    except json.JSONDecodeError:
        print(f"Error: Archivo JSON inválido en {ruta_archivo}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    ruta_archivo = r"C:\Users\INE_TSP3\Desktop\Paginas\publicacion\nacional\assets\configuracion.json"  # Reemplaza con tu ruta real

    # Lista de posibles parámetros (URLs, valores, etc.)
    parametros = [
        "./assets/20250601_2000_COMPUTOS.zip",
        "./assets/20250601_2005_COMPUTOS.zip",
        # ... más parámetros
    ]

    indice_parametro = 0  # Índice para recorrer la lista de parámetros

    # Bucle while que se ejecuta mientras haya parámetros disponibles
    while indice_parametro < len(parametros):
        nuevo_parametro = parametros[indice_parametro]
        actualizar_json(ruta_archivo, nuevo_parametro)

        indice_parametro += 1  # Avanzar al siguiente parámetro

        if indice_parametro < len(parametros):  # Esperar solo si hay más parámetros
            time.sleep(300)  # Esperar 300 segundos (5 minutos)

    print("Se han utilizado todos los parámetros. El script ha terminado.")