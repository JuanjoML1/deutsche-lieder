from bs4 import BeautifulSoup
import os

# Abrimos el index.html
with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Extraemos todos los enlaces dentro de ul.lista
enlaces = soup.select("ul.lista li a")

# Plantilla de canción
plantilla = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{titulo}</title>
<link rel="stylesheet" href="../../css/estilo.css">
</head>
<body>
<h1>{titulo}</h1>
<pre>
Aquí irá la letra...
</pre>
<a href="../../index.html">Volver al índice</a>
</body>
</html>
"""

# Creamos los archivos de cada canción
for a in enlaces:
    ruta = a['href']          # ej: "canciones/andrea_bouranis/auf_anderen_wegen.html"
    titulo = a.text.strip()   # ej: "Auf anderen Wegen"
    
    # Nos aseguramos de que la carpeta exista
    carpeta = os.path.dirname(ruta)
    os.makedirs(carpeta, exist_ok=True)
    
    # Creamos el archivo HTML si no existe
    if not os.path.exists(ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(plantilla.format(titulo=titulo))

print("Todos los HTMLs de canciones se han generado o comprobado correctamente!")
