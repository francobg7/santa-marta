"""
Script para crear imágenes de ejemplo del campo
Ejecutar este script para generar imágenes de prueba
"""

from reportlab.graphics.shapes import Drawing, Rect, String, Circle, Line
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.lib.units import cm
import os

def crear_imagen_ejemplo(numero, titulo, color_fondo, color_texto):
    """Crear una imagen de ejemplo para el campo"""
    drawing = Drawing(14*cm, 8*cm)
    
    # Fondo
    drawing.add(Rect(0, 0, 14*cm, 8*cm, fillColor=color_fondo, strokeColor=colors.black, strokeWidth=2))
    
    # Título
    drawing.add(String(7*cm, 6*cm, titulo, textAnchor="middle", 
                      fontSize=24, fillColor=color_texto))
    
    # Subtítulo
    drawing.add(String(7*cm, 5*cm, f"Vista {numero} del Campo", textAnchor="middle", 
                      fontSize=16, fillColor=color_texto))
    
    # Elementos decorativos
    drawing.add(Circle(2*cm, 2*cm, 0.5*cm, fillColor=colors.white, strokeColor=color_texto))
    drawing.add(Circle(12*cm, 2*cm, 0.5*cm, fillColor=colors.white, strokeColor=color_texto))
    drawing.add(Circle(7*cm, 1*cm, 0.3*cm, fillColor=colors.white, strokeColor=color_texto))
    
    # Líneas decorativas
    drawing.add(Line(1*cm, 3*cm, 13*cm, 3*cm, strokeColor=color_texto, strokeWidth=2))
    drawing.add(Line(1*cm, 1.5*cm, 13*cm, 1.5*cm, strokeColor=color_texto, strokeWidth=1))
    
    return drawing

def generar_imagenes_ejemplo():
    """Generar todas las imágenes de ejemplo"""
    imagenes_info = [
        (1, "Vista Principal", colors.HexColor('#27ae60'), colors.white),
        (2, "Pasturas Gatton Panic", colors.HexColor('#2ecc71'), colors.white),
        (3, "Área Agrícola", colors.HexColor('#f39c12'), colors.white),
        (4, "Zona de Monte", colors.HexColor('#8e44ad'), colors.white),
        (5, "Vista Panorámica", colors.HexColor('#3498db'), colors.white)
    ]
    
    print("🎨 Generando imágenes de ejemplo...")
    
    for numero, titulo, color_fondo, color_texto in imagenes_info:
        drawing = crear_imagen_ejemplo(numero, titulo, color_fondo, color_texto)
        
        # Guardar como PDF
        filename = f"campo{numero}.pdf"
        renderPDF.drawToFile(drawing, filename)
        
        print(f"✅ Generada: {filename}")
    
    print("\n📸 Imágenes de ejemplo creadas:")
    print("• campo1.pdf - Vista Principal")
    print("• campo2.pdf - Pasturas Gatton Panic") 
    print("• campo3.pdf - Área Agrícola")
    print("• campo4.pdf - Zona de Monte")
    print("• campo5.pdf - Vista Panorámica")
    print("\n💡 Para usar en el PDF, convierta estos archivos a JPG:")
    print("   - Use un convertidor online o software de imagen")
    print("   - Renombre como: campo1.jpg, campo2.jpg, etc.")
    print("   - O simplemente agregue sus propias fotos del campo")

if __name__ == "__main__":
    generar_imagenes_ejemplo()
