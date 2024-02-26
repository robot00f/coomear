from bs4 import BeautifulSoup
import requests

# Leer la lista de URLs desde el archivo
with open("lista.txt", "r") as file:
    urls = file.readlines()

# Iterar sobre cada URL en la lista
for url in urls:
    url = url.strip()  # Eliminar espacios en blanco al principio y al final
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontrar todos los elementos con la clase "fileThumb"
    file_thumbs = soup.find_all(class_="fileThumb")

    # Encontrar todos los elementos con la clase "post__attachment-link"
    attachment_links = soup.find_all(class_="post__attachment-link")

    # Crear un archivo de texto para guardar los enlaces de cada URL
    with open("enlaces.txt", "a") as file:
        # Guardar enlaces de fileThumb
        for file_thumb in file_thumbs:
            link = file_thumb.get("href")
            if link.endswith(".jpg") or link.endswith(".jpeg") or link.endswith(".png"):
                file.write(f"{link}\n")

        # Guardar enlaces de post__attachment-link
        for attachment_link in attachment_links:
            link = attachment_link.get("href")
            if link.endswith(".mp4"):
                file.write(f"{link}\n")

        file.write("\n")  # Separador entre URLs

print("Enlaces guardados en enlaces.txt")
