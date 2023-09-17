import pandas as pd
import os

# Leer el archivo CSV en un DataFrame
df = pd.read_csv("./data/RPT_RA_11_NOTAS_FINALES_POR_PERIODO_12023.csv")

#Eliminar columnas con data no manipunable
def eliminar_columna_textbox16(df):
    return df.drop(columns=['textbox16'], axis=1)

def eliminar_columna_textbox36(df):
    return df.drop(columns=['textbox36'], axis=1)

def eliminar_columna_textbox22(df):
    return df.drop(columns=['textbox22'], axis=1)

def eliminar_columna_textbox47(df):
    return df.drop(columns=['textbox47'], axis=1)

def eliminar_columna_textbox49(df):
    return df.drop(columns=['textbox49'], axis=1)

def eliminar_columna_textbox51(df):
    return df.drop(columns=['textbox51'], axis=1)

def eliminar_columna_textbox53(df):
    return df.drop(columns=['textbox53'], axis=1)

def eliminar_columna_textbox55(df):
    return df.drop(columns=['textbox55'], axis=1)

def eliminar_columna_textbox40(df):
    return df.drop(columns=['textbox40'], axis=1)

def eliminar_columna_GRPSTN(df):
    return df.drop(columns=['GRPSTN'], axis=1)

def eliminar_columna_textbox6(df):
    return df.drop(columns=['textbox6'], axis=1)

#Renombrar columnas textbox
def renombrar_columna_textbox32(df):
    return df.rename(columns={'textbox32': 'Carrera'})

def renombrar_columna_textbox46(df):
    return df.rename(columns={'textbox46': 'Materia'})

def renombrar_columna_textbox48(df):
    return df.rename(columns={'textbox48': 'CodClass'})

def renombrar_columna_textbox50(df):
    return df.rename(columns={'textbox50': 'Grupo'})

def renombrar_columna_textbox52(df):
    return df.rename(columns={'textbox52': 'Creditos'})

def renombrar_columna_textbox54(df):
    return df.rename(columns={'textbox54': 'CodProf'})

def renombrar_columna_textbox56(df):
    return df.rename(columns={'textbox56': 'Cuatrimestre'})


# Llamar a las funciones para eliminar las columnas
df = eliminar_columna_textbox16(df)
df = eliminar_columna_textbox22(df)
df = eliminar_columna_textbox47(df)
df = eliminar_columna_textbox36(df)
df = eliminar_columna_textbox40(df)
df= eliminar_columna_textbox49(df)
df= eliminar_columna_textbox51(df)
df = eliminar_columna_textbox53(df)
df = eliminar_columna_textbox55(df)
df = eliminar_columna_GRPSTN(df)
df = eliminar_columna_textbox6(df)

#Llamar a las funciones para renombrar las columnas
df = renombrar_columna_textbox32(df)
df = renombrar_columna_textbox46(df)
df = renombrar_columna_textbox48(df)
df = renombrar_columna_textbox50(df)
df = renombrar_columna_textbox52(df)
df = renombrar_columna_textbox54(df)
df = renombrar_columna_textbox56(df)
# Ruta y nombre del nuevo archivo CSV
archivo_csv = 'DATA_NORMALIZADA/RPT_RA_11_NOTAS_FINALES_POR_PERIODO_12023.csv'

# Crear la carpeta si no existe
carpeta = os.path.dirname(archivo_csv)
if not os.path.exists(carpeta):
    os.makedirs(carpeta)

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv(archivo_csv, index=False)
