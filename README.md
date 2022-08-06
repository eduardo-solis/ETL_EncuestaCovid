# ETL_EncuestaCovid
Practica del proceso de ETL para una encuesta sobre el covid

# Pasos preeliminares

1. Entrar al archivo `extract/main.py` y cambiar los datos de la conexion en dado caso que se tenga un usuario, contraseña y host direfentes
2. Abrir **MySQL Workbench** y ejecutar el archivo ubicado en `database/encuestacovid.sql`

# Como se ejecuta
Para ejecutar este proceso de ETL (Extract, Transform and Load) lo que se necesita es:

1. Tener instalado Anaconda
2. Dirigirse a la carpeta del proyecto
3. Ejecutar el comando `python pipeline.py "parametro"`

El parametro puede ser:

- 1: Para obtener la información de todas las carreras
- 2: Para obtener la información de la carrera de Desarrollo y Gestion de Software
- 3: Para obtener la información de la carrera de Redes
- 4: Para obtener la información de la carrera de Entornos

