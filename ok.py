import os
import requests

# Crear un directorio para guardar los archivos descargados
if not os.path.exists("descargas"):
    os.makedirs("descargas")

# Leer los enlaces desde el archivo
with open("enlaces.txt", "r") as file:
    links = file.readlines()

# Iterar sobre cada enlace
for link in links:
    link = link.strip()  # Eliminar espacios en blanco al principio y al final
    filename = link.split("/")[-1]  # Obtener el nombre del archivo de la URL

    # Limpiar el nombre del archivo de caracteres no válidos
    filename = ''.join(c for c in filename if c.isalnum() or c in ['.', '-', '_'])

    # Descargar el archivo si la URL no está vacía
    if link:
        response = requests.get(link)
        if response.status_code == 200:
            with open(f"descargas/{filename}", "wb") as file:
                file.write(response.content)
            print(f"Archivo descargado: {filename}")
        else:
            print(f"Error al descargar el archivo {filename}")
    else:
        print("URL vacía, omitiendo descarga.")

print("Descarga completada.")
