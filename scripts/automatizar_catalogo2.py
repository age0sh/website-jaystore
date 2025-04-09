from bs4 import BeautifulSoup

def agregar_relojes_nuevos(soup):
    footer = soup.find('div', class_='footer')
    current_number = 41
    
    # Calcular cantidad de bloques necesarios (4 relojes por bloque)
    bloques_necesarios = (70 - 40 + 3) // 4  # +3 para redondear hacia arriba
    
    for bloque in range(bloques_necesarios):
        # Crear contenedor principal
        relojes_div = soup.new_tag('div', **{'class': 'relojes'})
        collage_div = soup.new_tag('div', **{'class': 'collage'})
        relojes_div.append(collage_div)
        
        # Agregar 4 productos por bloque
        for _ in range(4):
            if current_number > 70:
                break
            
            # Crear estructura del producto
            producto_div = soup.new_tag('div', **{'class': 'producto'})
            
            # Contenedor imagen
            imagen_placeholder = soup.new_tag('div', **{'class': 'imagen-placeholder'})
            enlace = soup.new_tag('a', href=f'caballero html/c{current_number}.html')
            img = soup.new_tag('img', **{
                'class': 'reloj-imagen',
                'alt': f'Reloj {current_number}',
                'src': f'images/caballero/c{current_number}.jpeg',
                'onerror': "this.style.display='none'"
            })
            enlace.append(img)
            imagen_placeholder.append(enlace)
            
            # Nombre
            nombre = soup.new_tag('h3', **{'class': 'nombre-reloj'})
            nombre.string = 'Nombre de reloj'
            
            # Precio
            precio = soup.new_tag('p', **{'class': 'precio-reloj'})
            precio.string = 'MX$ XXXX'
            
            # Botón
            boton = soup.new_tag('button', **{'class': 'ordenar-reloj'})
            boton.string = 'Ordenar'
            
            # Ensamblar
            producto_div.append(imagen_placeholder)
            producto_div.append(nombre)
            producto_div.append(precio)
            producto_div.append(boton)
            
            collage_div.append(producto_div)
            current_number += 1
        
        # Insertar el bloque completo antes del footer
        footer.insert_before(relojes_div)
    
    return soup

# Uso:
with open('caballero.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

soup = agregar_relojes_nuevos(soup)

with open('caballero_actualizado.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))