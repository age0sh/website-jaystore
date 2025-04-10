import pandas as pd
from bs4 import BeautifulSoup

# Leer el archivo Excel
df = pd.read_excel('relojes.xlsx')

# Crear diccionario con datos
relojes_data = {}
for _, row in df.iterrows():
    if isinstance(row['id'], str) and row['id'].startswith('c'):
        relojes_data[row['id']] = {
            'nombre': row['nombre'],
            'precio': f"MX$ {int(row['precio'])}",
            'enlace': f"caballero html/{row['id']}.html"  # Ruta corregida
        }

# Leer HTML
with open('caballero.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Actualizar elementos
for i in range(1, 77):
    reloj_id = f'c{i}'
    if reloj_id in relojes_data:
        producto = soup.find_all('div', class_='producto')[i-1]
        
        # Actualizar nombre
        producto.find('h3', class_='nombre-reloj').string = relojes_data[reloj_id]['nombre']
        
        # Actualizar precio
        producto.find('p', class_='precio-reloj').string = relojes_data[reloj_id]['precio']
        
        # Actualizar enlace
        enlace = producto.find('div', class_='imagen-placeholder').a
        enlace['href'] = relojes_data[reloj_id]['enlace']

# Guardar cambios
with open('caballero_actualizado.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("Actualización completada: caballero_actualizado.html")