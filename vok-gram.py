import os
from bs4 import BeautifulSoup

# Carpeta principal de canciones
carpeta_canciones = "canciones"

# Plantilla de secciones nuevas
bloque_extra = """
    <hr>
    <h2>Vokabeln</h2>
    <div class="vocabulario">
    </div>
    <hr>
    <h2>Grammatik</h2>
    <div class="gramatica">
    </div>
"""

# Recorremos todos los archivos HTML dentro de la carpeta canciones
for root, dirs, files in os.walk(carpeta_canciones):
    for file in files:
        if file.endswith(".html"):
            ruta = os.path.join(root, file)
            
            with open(ruta, "r", encoding="utf-8") as f:
                html = f.read()
            
            # Parseamos el HTML con BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            
            # Buscamos el <a> de "Volver al índice"
            volver = soup.find("a", string="Volver al índice")
            if volver:
                # Solo añadimos si todavía no existe vocabulario/gramática
                if not soup.find("h2", string="Vokabeln"):
                    # Insertamos justo antes del enlace
                    bloque = BeautifulSoup(bloque_extra, "html.parser")
                    volver.insert_before(bloque)
                    
                    # Guardamos cambios
                    with open(ruta, "w", encoding="utf-8") as f:
                        f.write(str(soup))
                    print(f"Actualizado: {ruta}")
                else:
                    print(f"Ya tenía secciones: {ruta}")
