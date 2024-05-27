import pandas as pd
import glob
import os
import datetime

def consolidar():
    directorio = r'C:\CSV'
    os.makedirs(directorio, exist_ok=True)
    archivos_csv = glob.glob(os.path.join(directorio, '*.csv'))
    
    if not archivos_csv:
        print("No se encontraron archivos CSV en el directorio.")
        return
    
    nombre_columna = input("Ingrese columna que usará para eliminar duplicados: ")
    
    df_concatenado = pd.DataFrame()  # DataFrame vacío para concatenar los datos

    try:
        for archivo in archivos_csv:
            try:
                df = pd.read_csv(archivo, encoding='latin1')
                df_concatenado = pd.concat([df_concatenado, df], ignore_index=True)
            except pd.errors.ParserError as e:
                print(f"Error al leer el archivo '{archivo}': {str(e)}")
                return
        if nombre_columna not in df_concatenado.columns:
            print(f"La columna '{nombre_columna}' no existe en los archivos CSV válidos.")
            return

        try:
            df_sin_duplicados = df_concatenado.drop_duplicates(subset=[nombre_columna])
        except Exception as e:
            print(f"Error al eliminar duplicados: {str(e)}")
            return

        fecha_actual = datetime.datetime.now()
        fecha_formateada = fecha_actual.strftime("%Y-%m-%d")
        nombre_archivo = os.path.join(directorio, f"Matriz_{fecha_formateada}.csv")

        try:
            df_sin_duplicados.to_csv(nombre_archivo, index=False)
            print(f"Archivo consolidado guardado como: {nombre_archivo}")
        except Exception as e:
            print(f"Error al guardar el archivo consolidado: {str(e)}")
            return

    except Exception as e:
        print(f"Se produjo un error inesperado: {str(e)}")



