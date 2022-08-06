# Importamos la libreria argparse para generar un CLI
import argparse
# Importamos la libreria logging para mostrar mensajes al usuario
import logging
# Importamos la libreria de pandas para analisis de datos
import pandas as pd
# Importamos la libreria nltk para extraer tokens del texto
import nltk
from nltk.corpus import stopwords

#Definimos cuales son nuestros stop words, aquellas palabras que no entran dentro del análisis como artículos, pronombres, etc.
stop_words = set(stopwords.words('spanish'))

import datetime

# Le pasamos la configuracion basica al logging
logging.basicConfig(level=logging.INFO)

#Obtenemos una referencia al logger
logger = logging.getLogger(__name__)

# Definimos la funcion principal
def main(file_name):
    logger.info('..:: Iniciando el Proceso de limpieza de datos ::..')
    # Invocamos a la funcion para leer los datos
    df = _read_data(file_name)
    # Asignamos el id al dataframe
    df = _set_index(df)
    # Verificando la fecha y asignando la edad
    df = _check_date_age(df)
    # Obteniendo los stopwords
    df = _set_stopwords(df)
    # Invocamos a la funcion para guardar el df en un archivo
    _save_data_to_csv(df, file_name)

    return df

# Funcion que lee el data set creado en el proceso de extraccion
def _read_data(file_name):
    logger.info('Leyendo el archivo {}'.format(file_name))
    #Leemos el archvo csv y lo devolvemos el data frame
    return pd.read_csv(file_name, encoding='utf-8')

# Funcion que asigna el id al dataframe
def _set_index(df):
    return df.set_index("Id")

def _check_date_age(df):
    now = datetime.datetime.now()
    fechas = []
    edades = []
    i = 0
    while i < df["Pregunta3"].count():
        fecha = df.iloc[i,2]
        fecha_separada = fecha.split("-")
        try:
            fecha_registro = datetime.datetime(int(fecha_separada[0]), int(fecha_separada[1]), int(fecha_separada[2]))
            edad = now.year - fecha_registro.year
            if edad >= 18:
                fechas.append(fecha)
                edades.append(edad)
            else:
                print(df["Pregunta3"][i])
                df = df.drop([i], axis=0)
            i += 1
        except:
            df = df.drop([i], axis=0)
            i += 1
            continue
    df["Pregunta3"] = fechas
    df["Edad"] = edades
    return df

# Funcion que crea la columna que contiene los stopwords de la pregunta No.30
def _set_stopwords(df):
    separador = "|"
    df["Tokens"] = tokenize_column(df, "Pregunta30")
    
    # Formateando los tokens
    df["Tokens"] = df["Tokens"].apply(lambda tokens: separador.join(tokens))
    return df

#Definimos una función para obtener los tokens de una columna específica.
def tokenize_column(df, column_name):
    return (df
                .dropna() #Eliminamos filas con NA si aún hubiera algunas.
                .apply(lambda row: nltk.word_tokenize(row[column_name]), axis=1) #Obtenemos los tokens de todas la filas de la columna (column_name)
                .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens))) #Eliminamos todas las palabras que no sean alfanuméticas.
                .apply(lambda tokens: list(map(lambda token: token.lower(), tokens))) #convetir todos los tokens a minúsculas para compararlas con los stop_words
                .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list))) #eliminando los stop_words
            )

# Funcion que guarda el dataframe transformado en un archivo csv
def _save_data_to_csv(df, file_name):
    clean_filename = 'clean_{}'.format(file_name)
    logger.info("Guardando los datos limpios en el archivo: {}".format(clean_filename))
    df.to_csv(clean_filename)

if __name__=="__main__":
    # Creamos un nuevo parser de argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', help="La ruta al dataset sucio", type=str)

    # Parseamos los argumentos
    args = parser.parse_args()
    df = main(args.file_name)

    # Mostramos el DataFrame
    print(df)


