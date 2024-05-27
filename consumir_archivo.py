import pandas as pd
import datetime
def consumir_archivo():
    # Leer el archivo CSV
    df = pd.read_csv('C:\CSV\Matriz.csv')
    
    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now()

    # Formatear la fecha como una cadena (por ejemplo, "2024-05-23")
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")

    # Definir los parámetros
    nombre_columna          = input("Nombre de la columna en la que desea buscar")
    columna_a_buscar        = nombre_columna  # Cambia esto por el nombre de la columna que deseas buscar
    palabra                 = input("Palabra que desea buscar")
    palabra_a_buscar        = palabra# La palabra que estás buscando
    nuevo_valor_agregado    = input("Ingrese el valor que debe tener el nuevo dato para su nueva columna")
    nuevo_valor             = nuevo_valor_agregado          # El valor que deseas poner en la nueva columna si se encuentra la palabra

    # Crear la nueva columna con el valor definido si se encuentra la palabra
    nueva_columna = input("Ingrese el nombre de la nueva columna").lower()
    df[nueva_columna] = df[columna_a_buscar].apply(lambda x: nuevo_valor if palabra_a_buscar in str(x) else '')

    # Guardar el DataFrame modificado en un nuevo archivo CSV
    df.to_csv('C:\CSV\Matriz_final.csv', index=False)