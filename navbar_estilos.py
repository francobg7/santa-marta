"""
Diferentes estilos de Nav Bar para PDFs
Puedes copiar y pegar estos estilos en tu archivo principal
"""

from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm

def crear_navbar_estilo_1():
    """Nav Bar estilo corporativo clásico"""
    nav_data = [
        [
            Paragraph("🏠 <b>SANTA MARTA</b><br/><font size='8'>Inmobiliaria</font>", 
                     ParagraphStyle(name='NavBar', fontSize=12, leading=16, alignment=1, textColor=colors.white)),
            Paragraph("🏡<br/>Inicio", 
                     ParagraphStyle(name='NavItem', fontSize=9, leading=12, alignment=1, textColor=colors.white)),
            Paragraph("🏘️<br/>Propiedades", 
                     ParagraphStyle(name='NavItem', fontSize=9, leading=12, alignment=1, textColor=colors.white)),
            Paragraph("📋<br/>Servicios", 
                     ParagraphStyle(name='NavItem', fontSize=9, leading=12, alignment=1, textColor=colors.white)),
            Paragraph("📞<br/>Contacto", 
                     ParagraphStyle(name='NavItem', fontSize=9, leading=12, alignment=1, textColor=colors.white)),
            Paragraph("📱<br/>+595 981 123 456", 
                     ParagraphStyle(name='NavItem', fontSize=9, leading=12, alignment=1, textColor=colors.white))
        ]
    ]
    
    nav_table = Table(nav_data, colWidths=[3.5*cm, 2.2*cm, 2.2*cm, 2.2*cm, 2.2*cm, 3.5*cm])
    nav_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 10),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#34495e')),
    ]))
    return nav_table

def crear_navbar_estilo_2():
    """Nav Bar estilo moderno con gradiente"""
    nav_data = [
        [
            Paragraph("🏠 <b>SANTA MARTA</b>", 
                     ParagraphStyle(name='NavBar', fontSize=14, leading=18, alignment=0, textColor=colors.white)),
            Paragraph("Inicio • Propiedades • Servicios • Contacto", 
                     ParagraphStyle(name='NavItem', fontSize=10, leading=14, alignment=2, textColor=colors.white)),
            Paragraph("📞 +595 981 123 456", 
                     ParagraphStyle(name='NavItem', fontSize=10, leading=14, alignment=2, textColor=colors.white))
        ]
    ]
    
    nav_table = Table(nav_data, colWidths=[4*cm, 8*cm, 4*cm])
    nav_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),
        ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 15),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#2980b9')),
    ]))
    return nav_table

def crear_navbar_estilo_3():
    """Nav Bar estilo minimalista"""
    nav_data = [
        [
            Paragraph("SANTA MARTA", 
                     ParagraphStyle(name='NavBar', fontSize=16, leading=20, alignment=1, textColor=colors.HexColor('#2c3e50'))),
        ],
        [
            Paragraph("Inicio • Propiedades • Servicios • Contacto • +595 981 123 456", 
                     ParagraphStyle(name='NavItem', fontSize=10, leading=14, alignment=1, textColor=colors.HexColor('#7f8c8d')))
        ]
    ]
    
    nav_table = Table(nav_data, colWidths=[16*cm])
    nav_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#ecf0f1')),
        ('BACKGROUND', (0, 1), (0, 1), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2c3e50')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 12),
        ('LINEBELOW', (0, 0), (0, 0), 2, colors.HexColor('#bdc3c7')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#bdc3c7')),
    ]))
    return nav_table

def crear_navbar_estilo_4():
    """Nav Bar estilo elegante con sombra"""
    nav_data = [
        [
            Paragraph("🏠 <b>SANTA MARTA</b><br/><font size='8' color='#bdc3c7'>Inmobiliaria Premium</font>", 
                     ParagraphStyle(name='NavBar', fontSize=13, leading=17, alignment=0, textColor=colors.white)),
            Paragraph("🏡 Inicio", 
                     ParagraphStyle(name='NavItem', fontSize=10, leading=14, alignment=1, textColor=colors.white)),
            Paragraph("🏘️ Propiedades", 
                     ParagraphStyle(name='NavItem', fontSize=10, leading=14, alignment=1, textColor=colors.white)),
            Paragraph("📋 Servicios", 
                     ParagraphStyle(name='NavItem', fontSize=10, leading=14, alignment=1, textColor=colors.white)),
            Paragraph("📞 Contacto", 
                     ParagraphStyle(name='NavItem', fontSize=10, leading=14, alignment=1, textColor=colors.white)),
            Paragraph("📱<br/>+595 981 123 456", 
                     ParagraphStyle(name='NavItem', fontSize=9, leading=12, alignment=2, textColor=colors.white))
        ]
    ]
    
    nav_table = Table(nav_data, colWidths=[3*cm, 2.5*cm, 2.5*cm, 2.5*cm, 2.5*cm, 3*cm])
    nav_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#8e44ad')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (1, 0), (4, 0), 'CENTER'),
        ('ALIGN', (5, 0), (5, 0), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 12),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#9b59b6')),
        ('LINEBEFORE', (1, 0), (1, 0), 1, colors.HexColor('#9b59b6')),
        ('LINEBEFORE', (2, 0), (2, 0), 1, colors.HexColor('#9b59b6')),
        ('LINEBEFORE', (3, 0), (3, 0), 1, colors.HexColor('#9b59b6')),
        ('LINEBEFORE', (4, 0), (4, 0), 1, colors.HexColor('#9b59b6')),
        ('LINEBEFORE', (5, 0), (5, 0), 1, colors.HexColor('#9b59b6')),
    ]))
    return nav_table

# Ejemplo de uso:
if __name__ == "__main__":
    print("Estilos de Nav Bar disponibles:")
    print("1. Estilo Corporativo Clásico")
    print("2. Estilo Moderno con Gradiente") 
    print("3. Estilo Minimalista")
    print("4. Estilo Elegante con Sombra")
    print("\nPara usar un estilo, copia la función correspondiente a tu archivo principal.")
