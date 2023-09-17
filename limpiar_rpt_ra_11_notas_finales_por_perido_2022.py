import pandas as pd
import os

# Leer el archivo CSV en un DataFrame
df = pd.read_csv("./data/RPT_RA_11_NOTAS_FINALES_POR_PERIODO_22020.csv")

#Eliminar columnas con data no manipunable
def eliminar_columna_textbox36(df):
    return df.drop(columns=['textbox36'], axis=1)

def eliminar_columna_textbox40(df):
    return df.drop(columns=['textbox40'], axis=1)

def eliminar_columna_GRPSTN(df):
    return df.drop(columns=['GRPSTN'], axis=1)

def eliminar_columna_textbox6(df):
    return df.drop(columns=['textbox6'], axis=1)

#Renombrar columnas textbox
def renombrar_columna_textbox32(df):
    return df.rename(columns=['textbox32': 'Carrera'])
def renombrar_columna_textbox46(df):
def renombrar_columna_textbox48(df):
def renombrar_columna_textbox50(df):
def renombrar_columna_textbox52(df):
def renombrar_columna_textbox54(df):
def renombrar_columna_textbox56(df):


# Llamar a las funciones para eliminar las columnas
df = eliminar_columna_textbox36(df)
df = eliminar_columna_textbox40(df)
df = eliminar_columna_GRPSTN(df)
df = eliminar_columna_textbox6(df)

# Ruta y nombre del nuevo archivo CSV
archivo_csv = 'DATA_NORMALIZADA/RPT_RA_11_notas_finales_por_perido_2022.csv'

# Crear la carpeta si no existe
carpeta = os.path.dirname(archivo_csv)
if not os.path.exists(carpeta):
    os.makedirs(carpeta)

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv(archivo_csv, index=False)
