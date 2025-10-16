# 🏡 SANTA-MARTA – Professional PDF Generator for Farmland Listings

This project generates **professional PDFs** for farmland sales with detailed information, a photo gallery, and direct contact links to Google Drive.

## ✨ Main Features

- **🎨 Professional design** with icons and corporate colors  
- **📸 Photo gallery** with support for multiple images  
- **🔗 Direct links** to WhatsApp, Google Maps, and Google Drive  
- **📊 Detailed property information** with specific data  
- **🏢 Corporate navigation bar** with brand identity  
- **📱 Responsive** and optimized for A4 printing  

## 🚀 Requirements

- Python 3.13+  
- `reportlab` (already included in the virtual environment)  
- Farmland images (optional)

## 📦 Installation

1. **Activate the virtual environment:**
```bash
source venv/bin/activate
```

2. **Install dependencies (if needed):**
```bash
pip install reportlab
```

## 🎯 Quick Start

1. **Activate the virtual environment:**
```bash
source venv/bin/activate
```

2. **Generate the PDF:**
```bash
python generar_pdf_terreno.py
```

3. **The PDF will be generated as `campo_santa_marta.pdf`**

## 📸 Carousel-Style Gallery

### Gallery Structure
- **1 large main image** (12x8 cm) at the top  
- **4 small thumbnails** (3x2 cm each) below  
- **Descriptive titles** for each thumbnail  

### File Names
- `campo1.jpg` – **Main image** (General view of the property)  
- `campo2.jpg` – **Pastures** (Gatton Panic)  
- `campo3.jpg` – **Agricultural area** (191 Has)  
- `campo4.jpg` – **Forest area** (437 Has)  
- `campo5.jpg` – **Panoramic view** (Aerial view)

### Generate Example Images
```bash
# Basic images
python crear_imagenes_ejemplo.py

# Carousel-specific images
python crear_imagenes_carrusel.py
```

## 🔗 Google Drive Integration

### Set Up Links
1. Upload the photos to a Google Drive folder  
2. Share the folder publicly  
3. Copy the folder ID  
4. Replace `XXXXXXX` in the code with the actual ID  

### Automatic Links
- **WhatsApp:** Direct contact with predefined message  
- **Google Maps:** Exact field location  
- **Google Drive:** Complete photo gallery  

## 📋 Field Information

The PDF automatically includes:
- **📍 Location:** Santa Marta, Boquerón, Paraguay  
- **🌱 Land Use:** Mixed (Agricultural + Livestock)  
- **🌧️ Rainfall:** 800 mm per year  
- **📏 Total Area:** 1,747 hectares  
- **🌾 Breakdown:** Agricultural (191 Ha), Livestock (715 Ha), Forest (437 Ha)  
- **🗺️ Points of Interest:** Distances to major cities  

## 🎨 Customization

### Modify Information
Edit the variables in `generar_pdf_terreno.py`:
- `info_campo` – Field information  
- `puntos_interes` – Points of interest  
- `whatsapp_link` – WhatsApp contact link  
- `maps_link` – Google Maps link  
- `drive_link` – Google Drive link  

### Change Styles
Use the styles from `navbar_estilos.py`:
1. **Classic Corporate** – Dark blue  
2. **Modern Gradient** – Light blue  
3. **Minimalist** – Light gray  
4. **Elegant with Shadow** – Purple  

## 📁 Project Structure

```
SANTA-MARTA/
├── generar_pdf_terreno.py        # Main script
├── navbar_estilos.py             # Nav bar styles
├── crear_imagenes_ejemplo.py     # Basic image generator
├── crear_imagenes_carrusel.py    # Carousel image generator
├── INSTRUCCIONES_IMAGENES.md     # Image guide
├── INSTRUCCIONES_CARRUSEL.md     # Carousel-specific guide
├── README.md                     # This file
├── venv/                         # Virtual environment
├── campo_santa_marta.pdf         # Generated PDF
└── campo1-5.jpg                  # Example images
```

## 🔧 Configuration Files

- **`generar_pdf_terreno.py`** – Main script with full logic  
- **`navbar_estilos.py`** – Four different nav bar styles  
- **`crear_imagenes_ejemplo.py`** – Generates test images  
- **`INSTRUCCIONES_IMAGENES.md`** – Complete image guide  

## 📱 Technical Details

- **Format:** Optimized A4 PDF  
- **Images:** Supports JPG, PNG, GIF  
- **Links:** Clickable inside the PDF  
- **Icons:** Built-in emojis  
- **Colors:** Professional corporate palette  
- **Font:** Helvetica (multiple weights)  

## 🎯 Use Cases

- **Real Estate Agencies** – Field presentation materials  
- **Agents** – Marketing and client brochures  
- **Landowners** – Direct property sales  
- **Investors** – Property analysis  

## 📞 Support

For further customization or assistance:
- Review `INSTRUCCIONES_IMAGENES.md`  
- Modify variables in the main code  
- Use predefined styles in `navbar_estilos.py`

The PDF is ready to use with Google Drive and direct contact links! 🚀  

# santa-marta
