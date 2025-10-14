"""
Script para crear imágenes de ejemplo específicas para el carrusel
Genera campo1.jpg (imagen principal) y campo2-5.jpg (miniaturas)
"""

from reportlab.graphics.shapes import Drawing, Rect, String, Circle, Line, Polygon
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.lib.units import cm
import os

def crear_imagen_principal():
    """Crear imagen principal del campo (campo1.jpg)"""
    drawing = Drawing(14*cm, 9*cm)
    
    # Fondo con gradiente simulado
    drawing.add(Rect(0, 0, 14*cm, 9*cm, fillColor=colors.HexColor('#27ae60'), strokeColor=colors.black, strokeWidth=3))
    
    # Título principal
    drawing.add(String(7*cm, 7*cm, "CAMPO SANTA MARTA", textAnchor="middle", 
                      fontSize=28, fillColor=colors.white))
    
    # Subtítulo
    drawing.add(String(7*cm, 6*cm, "Vista Principal - 1.747 Has", textAnchor="middle", 
                      fontSize=16, fillColor=colors.white))
    
    # Elementos decorativos del campo
    # Pasturas (rectángulos verdes)
    drawing.add(Rect(1*cm, 1*cm, 4*cm, 2*cm, fillColor=colors.HexColor('#2ecc71'), strokeColor=colors.white))
    drawing.add(Rect(9*cm, 1*cm, 4*cm, 2*cm, fillColor=colors.HexColor('#2ecc71'), strokeColor=colors.white))
    
    # Área agrícola (rectángulo amarillo)
    drawing.add(Rect(5*cm, 1*cm, 4*cm, 2*cm, fillColor=colors.HexColor('#f39c12'), strokeColor=colors.white))
    
    # Monte (rectángulo marrón)
    drawing.add(Rect(2*cm, 3*cm, 4*cm, 2*cm, fillColor=colors.HexColor('#8b4513'), strokeColor=colors.white))
    
    # Líneas de división
    drawing.add(Line(0, 3*cm, 14*cm, 3*cm, strokeColor=colors.white, strokeWidth=2))
    drawing.add(Line(7*cm, 0, 7*cm, 9*cm, strokeColor=colors.white, strokeWidth=1))
    
    return drawing

def crear_miniatura_pasturas():
    """Crear miniatura de pasturas (campo2.jpg)"""
    drawing = Drawing(4*cm, 3*cm)
    
    # Fondo verde
    drawing.add(Rect(0, 0, 4*cm, 3*cm, fillColor=colors.HexColor('#27ae60'), strokeColor=colors.black))
    
    # Título
    drawing.add(String(2*cm, 2*cm, "PASTURAS", textAnchor="middle", 
                      fontSize=14, fillColor=colors.white))
    
    # Subtítulo
    drawing.add(String(2*cm, 1.5*cm, "Gatton Panic", textAnchor="middle", 
                      fontSize=10, fillColor=colors.white))
    
    # Elementos decorativos
    drawing.add(Circle(1*cm, 0.5*cm, 0.2*cm, fillColor=colors.white))
    drawing.add(Circle(3*cm, 0.5*cm, 0.2*cm, fillColor=colors.white))
    
    return drawing

def crear_miniatura_agricola():
    """Crear miniatura agrícola (campo3.jpg)"""
    drawing = Drawing(4*cm, 3*cm)
    
    # Fondo amarillo
    drawing.add(Rect(0, 0, 4*cm, 3*cm, fillColor=colors.HexColor('#f39c12'), strokeColor=colors.black))
    
    # Título
    drawing.add(String(2*cm, 2*cm, "AGRÍCOLA", textAnchor="middle", 
                      fontSize=14, fillColor=colors.white))
    
    # Subtítulo
    drawing.add(String(2*cm, 1.5*cm, "191 Has", textAnchor="middle", 
                      fontSize=10, fillColor=colors.white))
    
    # Elementos decorativos
    drawing.add(Rect(0.5*cm, 0.5*cm, 3*cm, 0.3*cm, fillColor=colors.white))
    drawing.add(Rect(0.5*cm, 1*cm, 3*cm, 0.3*cm, fillColor=colors.white))
    
    return drawing

def crear_miniatura_monte():
    """Crear miniatura de monte (campo4.jpg)"""
    drawing = Drawing(4*cm, 3*cm)
    
    # Fondo marrón
    drawing.add(Rect(0, 0, 4*cm, 3*cm, fillColor=colors.HexColor('#8b4513'), strokeColor=colors.black))
    
    # Título
    drawing.add(String(2*cm, 2*cm, "MONTE", textAnchor="middle", 
                      fontSize=14, fillColor=colors.white))
    
    # Subtítulo
    drawing.add(String(2*cm, 1.5*cm, "437 Has", textAnchor="middle", 
                      fontSize=10, fillColor=colors.white))
    
    # Elementos decorativos (árboles como círculos)
    drawing.add(Circle(1.5*cm, 1*cm, 0.3*cm, fillColor=colors.white))
    drawing.add(Circle(3*cm, 1*cm, 0.3*cm, fillColor=colors.white))
    
    return drawing

def crear_miniatura_panoramica():
    """Crear miniatura panorámica (campo5.jpg)"""
    drawing = Drawing(4*cm, 3*cm)
    
    # Fondo azul (cielo)
    drawing.add(Rect(0, 0, 4*cm, 3*cm, fillColor=colors.HexColor('#3498db'), strokeColor=colors.black))
    
    # Título
    drawing.add(String(2*cm, 2*cm, "PANORÁMICA", textAnchor="middle", 
                      fontSize=12, fillColor=colors.white))
    
    # Subtítulo
    drawing.add(String(2*cm, 1.5*cm, "Vista aérea", textAnchor="middle", 
                      fontSize=10, fillColor=colors.white))
    
    # Elementos decorativos (nubes)
    drawing.add(Circle(1*cm, 2.5*cm, 0.3*cm, fillColor=colors.white))
    drawing.add(Circle(1.3*cm, 2.5*cm, 0.2*cm, fillColor=colors.white))
    drawing.add(Circle(3*cm, 2.2*cm, 0.25*cm, fillColor=colors.white))
    
    return drawing

def generar_imagenes_carrusel():
    """Generar todas las imágenes para el carrusel"""
    print("🎨 Generando imágenes para galería tipo carrusel...")
    
    # Imagen principal
    drawing_principal = crear_imagen_principal()
    renderPDF.drawToFile(drawing_principal, "campo1.pdf")
    print("✅ Generada: campo1.pdf - Imagen principal (12x8 cm)")
    
    # Miniaturas
    miniaturas = [
        (crear_miniatura_pasturas(), "campo2.pdf", "Pasturas Gatton Panic"),
        (crear_miniatura_agricola(), "campo3.pdf", "Área Agrícola"),
        (crear_miniatura_monte(), "campo4.pdf", "Zona de Monte"),
        (crear_miniatura_panoramica(), "campo5.pdf", "Vista Panorámica")
    ]
    
    for drawing, filename, descripcion in miniaturas:
        renderPDF.drawToFile(drawing, filename)
        print(f"✅ Generada: {filename} - {descripcion} (3x2 cm)")
    
    print("\n📸 Imágenes del carrusel creadas:")
    print("• campo1.pdf - Imagen principal (Vista general del campo)")
    print("• campo2.pdf - Pasturas Gatton Panic")
    print("• campo3.pdf - Área Agrícola")
    print("• campo4.pdf - Zona de Monte")
    print("• campo5.pdf - Vista Panorámica")
    print("\n💡 Para usar en el PDF:")
    print("   1. Convierta los archivos PDF a JPG")
    print("   2. Renombre como: campo1.jpg, campo2.jpg, etc.")
    print("   3. Coloque en el directorio del proyecto")
    print("   4. Ejecute: python generar_pdf_terreno.py")

if __name__ == "__main__":
    generar_imagenes_carrusel()
