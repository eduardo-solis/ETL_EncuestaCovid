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
def _form_scrapper(carrera):
    logger.info('..:: Iniciando el scrapper para la obtención del formulario ::..')
    cursor = conn.cursor()
    sql = ""

    if carrera == "1":
        sql = "SELECT * FROM formulario"
    if carrera == "2":
        sql = "SELECT * FROM formulario WHERE pregunta_5 = 'Ingenieria en Desarrollo y Gestion de Software'"
    if carrera == "3":
        sql = "SELECT * FROM formulario WHERE pregunta_5 = 'Ingeniería en Redes y Ciberseguridad'"
    if carrera == "4":
        sql = "SELECT * FROM formulario WHERE pregunta_5 = 'Ingeniería en Entornos Virtuales y Negocios Digitales'"

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

            p13_1 = str(formulario[13]).replace(", ", "|").replace(",", "|").replace("\"", "")
            p13_l = len(p13_1)
            p13 = p13_1[:p13_l-1]

            p15_1 = str(formulario[15]).replace(", ", "|").replace(",", "|").replace("\"", "")
            p15_l = len(p15_1)
            p15 = p15_1[:p15_l-1]

            p16_1 = str(formulario[16]).replace(", ", "|").replace(",", "|").replace("\"", "")
            p16_l = len(p16_1)
            p16 = p16_1[:p16_l-1]

            p17_1 = str(formulario[17]).replace(", ", "|").replace(",", "|").replace("\"", "")
            p17_l = len(p17_1)
            p17 = p17_1[:p17_l-1]

            p18_1 = str(formulario[18]).replace(", ", "|").replace(",", "|").replace("\"", "")
            p18_l = len(p18_1)
            p18 = p18_1[:p18_l-1]

            p28_1 = str(formulario[28]).replace(", ", "|").replace(",", "|").replace("\"", "")
            p28_l = len(p28_1)
            p28 = p28_1[:p28_l-1]

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

    # Creando un nuevo parser
    parser = argparse.ArgumentParser()

    # Creando la lista de opciones
    opciones = ["1","2","3","4"]
    
    # 1 - Todas las carreras
    # 2 - Ingeniería en Desarrollo y Gestión de Software
    # 3 - Ingeniería en Redes y Ciberseguridad
    # 4 - Ingeniería en Entornos Virtuales y Negocios Digitales

    # Añadiendo argumentos (obligatorios) y ayuda al parser
    parser.add_argument('carrera',
                        help="Carrera de la utl que quiere escrapear",
                        type = str,
                        choices=opciones)

    # Parseamos los argumentos y nos devuelve un objeto con ellos.
    args = parser.parse_args()
    print(args)
    # Llammamos a la funcion para recuperar las url's
    _form_scrapper(args.carrera)
