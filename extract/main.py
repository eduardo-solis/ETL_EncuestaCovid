# Importación de las librerias necesarias
import argparse #Parseador de argumentos
import logging #Para mostrar mensajes en consola
import csv
import datetime
from os import write

# Importamos la libreria para la conexion con la base de datos
from mysql.connector import connect

# Importamos los errores
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

# Le damos la configuracion basica al logging
logging.basicConfig(level=logging.INFO)

# Obtenemos una referencia al logger
logger = logging.getLogger(__name__)

# Creamos la conexion con la base de datos
conn = connect(user='root', password='root', host='127.0.0.1', database='encuestacovid')

# Funcion para obtener los datos de la encuesta
def _form_scrapper():
    logger.info('..:: Iniciando el scrapper para la obtención del formulario ::..')
    cursor = conn.cursor()
    sql = "SELECT * FROM formulario"
    cursor.execute(sql)
    formularios = cursor.fetchall()
    conn.close()
    _save_form(formularios)
    print(f'Num. Formularios {str(len(formularios))}')

# Funcion para guardar los datos del formulario
def _save_form(formularios):
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = 'formularios_{}.csv'.format(now)
    csv_headers = ['Id', 'Pregunta1','Pregunta2','Pregunta3',
                    'Pregunta4', 'Pregunta5', 'Pregunta6',
                    'Pregunta7', 'Pregunta8', 'Pregunta9',
                    'Pregunta10','Pregunta11','Pregunta12',
                    'Pregunta13','Pregunta14','Pregunta15',
                    'Pregunta16','Pregunta17','Pregunta18',
                    'Pregunta19','Pregunta20','Pregunta21',
                    'Pregunta22','Pregunta23','Pregunta24',
                    'Pregunta25','Pregunta26','Pregunta27',
                    'Pregunta28','Pregunta29','Pregunta30',
                    'Fecha']
    # Escribimos en el archivo
    with open(out_file_name, mode='w+', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)
        for formulario in formularios:

            p13 = str(formulario[13]).replace(", ", "|")
            p15 = str(formulario[15]).replace(", ", "|")
            p16 = str(formulario[16]).replace(", ", "|")
            p17 = str(formulario[17]).replace(", ", "|")
            p18 = str(formulario[18]).replace(", ", "|")
            p28 = str(formulario[28]).replace(", ", "|")
            p30 = str(formulario[30]).replace(",", " ").replace("  ", " ")

            row = [formulario[0],formulario[1],formulario[2],
                    formulario[3],formulario[4],formulario[5],
                    formulario[6],formulario[7],formulario[8],
                    formulario[9],formulario[10],formulario[11],
                    formulario[12],p13,formulario[14],
                    p15,p16,p17,p18,formulario[19],
                    formulario[20],formulario[21],formulario[22],
                    formulario[23],formulario[24],formulario[25],
                    formulario[26],formulario[27],p28,formulario[29],
                    p30,formulario[31]]
            writer.writerow(row)

if __name__=='__main__':
    _form_scrapper()
