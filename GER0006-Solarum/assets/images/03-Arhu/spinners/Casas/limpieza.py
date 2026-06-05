import os
import re

def procesar_imagenes(carpeta):
    if not os.path.exists(carpeta):
        print(f"Error: La carpeta '{carpeta}' no existe.")
        return

    print("Iniciando limpieza...")

    # 1. Eliminar todos los archivos .webp
    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith('.webp'):
            ruta_completa = os.path.join(carpeta, archivo)
            os.remove(ruta_completa)
            print(f"Eliminado (.webp): {archivo}")

    # 2. Recopilar los .jpg y aplicar reglas de eliminación
    archivos_jpg = [f for f in os.listdir(carpeta) if f.lower().endswith('.jpg')]
    archivos_a_renombrar = []

    for archivo in archivos_jpg:
        match = re.search(r'^(.*)_(\d+)\.jpg$', archivo, re.IGNORECASE)
        if match:
            base = match.group(1)
            numero = int(match.group(2))
            ruta_completa = os.path.join(carpeta, archivo)

            if numero == 1 or (5 <= numero <= 22):
                os.remove(ruta_completa)
                print(f"Eliminado (.jpg): {archivo}")
            else:
                archivos_a_renombrar.append((base, numero, archivo))

    # --- LA SOLUCIÓN ESTÁ AQUÍ ---
    # Ordenamos la lista basándonos en el 'numero' de menor a mayor.
    # Así el _3 se renombra a _10 ANTES de que el _25 intente convertirse en _3.
    archivos_a_renombrar.sort(key=lambda x: x[1])

    print("\nIniciando renombramiento...")

    # 3. Renombrar los archivos restantes
    for base, numero, archivo_original in archivos_a_renombrar:
        nuevo_numero = None
        
        if numero == 2:
            nuevo_numero = 9
        elif numero == 3:
            nuevo_numero = 10
        elif numero == 4:
            nuevo_numero = 11
        elif 23 <= numero <= 30:
            nuevo_numero = numero - 22 
        
        if nuevo_numero is not None:
            ruta_original = os.path.join(carpeta, archivo_original)
            nuevo_nombre = f"{base}_{nuevo_numero}.jpg"
            ruta_nueva = os.path.join(carpeta, nuevo_nombre)
            
            os.rename(ruta_original, ruta_nueva)
            print(f"Renombrado: {archivo_original}  ->  {nuevo_nombre}")

    print("\n¡Proceso terminado con éxito!")

# Cambia la ruta por tu ruta real (manteniendo la 'r' inicial)
ruta_de_tu_carpeta = r"G:\archibot-web\clients\ger\GER0006-Solarum\assets\images\03-Arhu\spinners\Casas\3-80" 

procesar_imagenes(ruta_de_tu_carpeta)