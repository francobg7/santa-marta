"""
Configuración del proyecto SANTA-MARTA PDF Generator
"""

# === INFORMACIÓN DEL CAMPO ===
CAMPO_INFO = {
    'nombre': 'SANTA MARTA',
    'ubicacion': 'Santa Marta, Boquerón, Paraguay',
    'aptitud': 'Mixto (Agrícola + Ganadero)',
    'precipitacion': '800 mm',
    'superficie_total': '1.747 Has',
    'agricolas': '191 Has',
    'ganaderas': '715 Has',
    'monte': '437 Has',
    'desarrollables': '154 Has',
    'excedente': '103 Has'
}

# === PUNTOS DE INTERÉS ===
PUNTOS_INTERES = [
    ('Ruta de la leche', '76 km'),
    ('Neuland', '150 km'),
    ('Filadelfia', '190 km'),
    ('Mariscal Estigarribia', '250 km'),
    ('Asunción', '500 km')
]

# === CONTACTO ===
CONTACTO = {
    'whatsapp': '+595 981 240 099',
    'whatsapp_link': 'https://wa.me/595981240099?text=Hola%2C%20vi%20el%20campo%20en%20venta%20en%20Santa%20Marta%2C%20Boquerón',
    'maps_link': 'https://maps.google.com/?q=-23.2984734,-60.5146408',
    'drive_link': 'https://drive.google.com/drive/folders/1IQy8Cjl1nAqoKcUkeSIh0thIItwWwYWq?usp=drive_link'
}

# === CONFIGURACIÓN DE IMÁGENES ===
IMAGENES = {
    'principal': 'campo1.jpg',
    'miniaturas': [
        ('campo2.jpg', 'Pasturas'),
        ('campo3.jpg', 'Agrícola'),
        ('campo4.jpg', 'Monte'),
        ('campo5.jpg', 'Panorámica')
    ]
}

# === CONFIGURACIÓN DEL PDF ===
PDF_CONFIG = {
    'nombre_archivo': 'campo_santa_marta.pdf',
    'tamaño_pagina': 'A4',
    'imagen_principal_ancho': 20,  # cm
    'imagen_principal_alto': 12,   # cm
    'miniatura_ancho': 5,          # cm
    'miniatura_alto': 3            # cm
}
