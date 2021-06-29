
#### Nombre del Proyecto: Api_Rest

## Introducción

El objetivo de este proyecto crear un script para extraer la información del dataset ubicado en la API de FUT21 y agregarla a una base de datos para permitir la consulta y modificación de datos allí guardados.
Url Api: https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1


#### Instalación :

* 1. Crear ambiente virtual dentro de la carpeta del proyecto

  > pip install virtualenv (si no lo tiene instalado)
  > virtualenv venv
  >
* 2. Luego debe activar el entorno virtual

  > .\ venv\Scripts\activate

* 3. Instalar librerias que se encuentra en archivo requeriments.txt

  > pip install -r requeriments.txt

* 4.Elimar el archivo con el nombre "0001_initial.py" que se encuentra en la carpeta:
    > team_players:
      > Migrations:
        > 0001_initial.py
* 5. Elimnar la BD llamada: db.sqlite3

* 6. Ejecución de los siguiente comandos:
    > python manage.py makemigrations snippets. 
    > 
    >  python manage.py migrate. 
    
* 7. Creación de usuario para BD
    > python manage.py createsuperuser 


#### Ejecución:

* 1. python manage.py runserver

  

## Versión (Python 3.7)
