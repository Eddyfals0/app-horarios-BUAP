import os
import sys
# Asegurarse de tener pdf2docx instalado: pip install pdf2docx
from pdf2docx import Converter
# Importar la función existente del extractor
# Asegúrate de que extractor_docx.py esté en el mismo directorio
from extractor_docx import docx_to_csv

def main():
    # Directorios base
    base_dir = os.getcwd()
    pdf_dir = os.path.join(base_dir, 'pdf')
    output_dir = os.path.join(base_dir, 'prueba extraxion')

    # Verificar existencia de carpeta origen
    if not os.path.exists(pdf_dir):
        print(f"[Error] No se encontró la carpeta 'pdf' en: {pdf_dir}")
        return

    # Crear carpeta destino si no existe
    if not os.path.exists(output_dir):
        print(f"Creando carpeta destino: {output_dir}")
        os.makedirs(output_dir)
    
    # Obtener lista de archivos PDF
    archivos = os.listdir(pdf_dir)
    pdfs = [f for f in archivos if f.lower().endswith('.pdf')]
    
    if not pdfs:
        print("No se encontraron archivos .pdf en la carpeta 'pdf'.")
        return
    
    print(f"Se encontraron {len(pdfs)} archivos PDF. Iniciando conversión masiva...")

    for archivo_pdf in pdfs:
        path_pdf = os.path.join(pdf_dir, archivo_pdf)
        
        # Nombre del archivo salida (mismo nombre pero .docx)
        nombre_docx = os.path.splitext(archivo_pdf)[0] + '.docx'
        path_docx = os.path.join(output_dir, nombre_docx)
        
        print(f"\n---------------------------------------------------")
        print(f"Procesando: {archivo_pdf}")
        
        # 1. Convertir PDF -> DOCX
        try:
            print(f" -> Convirtiendo a DOCX...")
            cv = Converter(path_pdf)
            cv.convert(path_docx)
            cv.close()
            print(f" -> DOCX guardado en: {path_docx}")
        except Exception as e:
            print(f"[Error] Falló la conversión a DOCX: {e}")
            continue # Saltar al siguiente si falla la conversión
            
        # 2. Llamar al extractor (DOCX -> CSV)
        try:
            print(f" -> Extrayendo información a CSV...")
            docx_to_csv(path_docx)
            # docx_to_csv imprime sus propios logs de éxito/error
        except Exception as e:
            print(f"[Error] Falló la extracción de datos: {e}")

    print("\n---------------------------------------------------")
    print("Proceso masivo completado.")

if __name__ == "__main__":
    main()
