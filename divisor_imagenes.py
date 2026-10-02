import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def split_image(image_path, rows=4, cols=4):
    try:
        # Abrir la imagen
        img = Image.open(image_path)
        img_width, img_height = img.size
        
        # Calcular el ancho y alto de cada una de las 16 celdas
        piece_width = img_width // cols
        piece_height = img_height // rows
        
        # Crear una carpeta para guardar los recortes
        base_name = os.path.basename(image_path)
        name, ext = os.path.splitext(base_name)
        if not ext:
            ext = ".jpg" # Por defecto si no tiene
            
        output_dir = os.path.join(os.path.dirname(image_path), f"{name}_16_partes")
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        count = 1
        for row in range(rows):
            for col in range(cols):
                # Calcular coordenadas del rectángulo (left, upper, right, lower)
                left = col * piece_width
                upper = row * piece_height
                
                # Para evitar problemas de redondeo en los últimos píxeles
                right = left + piece_width if col < cols - 1 else img_width
                lower = upper + piece_height if row < rows - 1 else img_height
                
                bbox = (left, upper, right, lower)
                
                # Recortar y guardar
                piece = img.crop(bbox)
                
                # Usar ceros a la izquierda para que se ordenen bien alfabéticamente (01, 02.. 16)
                output_path = os.path.join(output_dir, f"{name}_parte_{count:02d}{ext}")
                piece.save(output_path)
                count += 1
                
        messagebox.showinfo(
            "¡Éxito!", 
            f"Se han guardado exitosamente las 16 imágenes en:\n\n{output_dir}\n\n"
            f"La foto ha sido dividida en una cuadrícula de {rows}x{cols}."
        )
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al procesar la imagen:\n\n{e}")

def select_file():
    # Abrir diálogo para seleccionar el archivo
    file_path = filedialog.askopenfilename(
        title="Selecciona la foto a dividir",
        filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.bmp *.webp *.tiff")]
    )
    if file_path:
        # Llamar a la función que divide la imagen
        split_image(file_path, rows=4, cols=4)

if __name__ == "__main__":
    # Configuración de la ventana principal
    root = tk.Tk()
    root.title("Divisor de Fotos para Póster (16 Partes)")
    root.geometry("450x250")
    
    # Intenta centrar un poco la ventana
    root.eval('tk::PlaceWindow . center')

    # Etiqueta de instrucciones
    instructions = (
        "Herramienta para dividir una foto en 16 partes (4x4).\n\n"
        "Ideal para imprimir pósters en tamaño A0 juntando\n"
        "varias impresiones más pequeñas (A3 o A4)."
    )
    
    label = tk.Label(root, text=instructions, font=("Helvetica", 11), justify="center")
    label.pack(pady=20)
    
    # Botón principal
    btn = tk.Button(
        root, 
        text="Seleccionar Foto y Dividir", 
        command=select_file, 
        font=("Helvetica", 12, "bold"), 
        bg="#0078D7", 
        fg="white", 
        padx=15, 
        pady=10,
        cursor="hand2"
    )
    btn.pack(pady=10)
    
    # Iniciar la interfaz gráfica
    root.mainloop()
