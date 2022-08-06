import argparse
import logging
import pandas as pd

import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Metodo para iniciar la aplicacion
def main(filename):
    
    # Leemos el archivo csv
    formularios = pd.read_csv(filename, encoding='utf-8')
    data = {}
    data['formularios'] = []
    # Iteramos entre la fila del csv mediante el metodo iterrows() y vamos pasando los articulos a la BD
    for index, row in formularios.iterrows():
        logger.info('Cargando el formulario con el id: {} en la BD'.format(row['Id']))

        if(len(str(row['Tokens'])) == 3):
            row['Tokens'] = "nada"

        formulario = {
            'id' : row['Id'],
            'pregunta1' : row['Pregunta1'],
            'pregunta2' : row['Pregunta2'],
            'pregunta3' : row['Pregunta3'],
            'pregunta4' : row['Pregunta4'],
            'pregunta5' : row['Pregunta5'],
            'pregunta6' : row['Pregunta6'],
            'pregunta7' : row['Pregunta7'],
            'pregunta8' : row['Pregunta8'],
            'pregunta9' : row['Pregunta9'],
            'pregunta10' : row['Pregunta10'],
            'pregunta11' : row['Pregunta11'],
            'pregunta12' : row['Pregunta12'],
            'pregunta13' : row['Pregunta13'],
            'pregunta14' : row['Pregunta14'],
            'pregunta15' : row['Pregunta15'],
            'pregunta16' : row['Pregunta16'],
            'pregunta17' : row['Pregunta17'],
            'pregunta18' : row['Pregunta18'],
            'pregunta19' : row['Pregunta19'],
            'pregunta20' : row['Pregunta20'],
            'pregunta21' : row['Pregunta21'],
            'pregunta22' : row['Pregunta22'],
            'pregunta23' : row['Pregunta23'],
            'pregunta24' : row['Pregunta24'],
            'pregunta25' : row['Pregunta25'],
            'pregunta26' : row['Pregunta26'],
            'pregunta27' : row['Pregunta27'],
            'pregunta28' : row['Pregunta28'],
            'pregunta29' : row['Pregunta29'],
            'pregunta30' : row['Pregunta30'],
            'fecha' : row['Fecha'],
            'edad' : row['Edad'],
            'tokens' : row['Tokens']
        }
        data['formularios'].append(formulario)
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == '__main__':
    #Creamos un nuevo parser de argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name',
                        help='La ruta al data set limpio para cargar a la base de datos',
                        type=str)
    #Parseamos los argumentos.
    args = parser.parse_args()
    main(args.file_name)