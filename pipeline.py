import datetime
#Permite invocar comandos del sistema operativo
import subprocess
import logging
import argparse #Parseador de argumentos

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Función principal que ejecuta el ETL paso a paso
def main(carrera):
    _extract(carrera)
    _transform()
    _load()
    logger.info('..::Proceso ETL finalizado::..')

#Función encargada de invocar el proceso de extracción
def _extract(carrera):
    logger.info('..::Iniciando el proceso de extracción::..')

    # Corremos un subproceso para ejecutar la primera etapa de extraccion en la carpeta /extract
    subprocess.run(['python', 'main.py', carrera], cwd='./extract')
    # Movemos el archivo csv generado al directorio transform
    subprocess.run(['move', r'extract\*.csv', r'transform'], shell=True)

#Función encargada de invocar el proceso de transformación
def _transform():
    logger.info('..::Iniciando el proceso de transformación::..')
    now = datetime.datetime.now().strftime('%Y_%m_%d')

    # Formando el nombre del archivo a procesar
    dirty_data_filename = 'formularios_{datetime}.csv'.format(datetime = now)

    # Corremos un subproceso para ejecutar la segunda etapa de transformacion en la carpeta /transform
    subprocess.run(['python', 'main.py', dirty_data_filename], cwd = './transform')
        
    # Borramos todos los data set sucios
    subprocess.run(['del', dirty_data_filename], shell = True, cwd='./transform')

    # Movemos los archivos csv generados al directorio load
    subprocess.run(['move', r'transform\*.csv', r'load'], shell = True)

#Función encargada de invocar el proceso de carga
def _load():
    logger.info('..::Iniciando el proceso de carga::..')
    now = datetime.datetime.now().strftime('%Y_%m_%d')

    # Fromando el nombre del archivo a procesar
    clean_data_filename = 'clean_formularios_{datetime}.csv'.format(datetime = now)

    # Corremos un subproceso para ejecutar la tercera etapa de carga en la carpeta /load
    subprocess.run(['python', 'main.py', clean_data_filename], cwd = './load')
        
    # Borramos todos los data set limpio
    subprocess.run(['del', clean_data_filename], shell = True, cwd='./load')


if __name__ == '__main__':
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
    main(args.carrera)