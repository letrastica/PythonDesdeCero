# Requerimientos 
## Instalando Python
- **Python** 
  - [MAC](https://www.freecodecamp.org/espanol/news/como-instalar-python-3-en-mac-tutorial-de-actualizacion-de-la-instalacion-de-brew/) 
  - [Windows](https://www.python.org/downloads/windows/)


Si ya tiene Python puedes verificarlo al abrir la terminal:

* **En windows**: Presiona la tecla windows, posteriormente escribe 'cmd' 
* **En Mac: Finder** - Abre la Terminal
  
Posteriormente escribe el siguiente comando:

``python --version``

Al ejecutar el comando te mostrará la versión que tienes actualmente instalada, para este entrenamiento, utilizaremos de la versión 3 para arriba.

## Instalando VS Code
Haz clic en el siguiente enlace [Visual Studio Code](https://code.visualstudio.com/) selecciona el sistema operativo de tu preferencia. Si no ves la opción de tu sistema.

## Instalando GitHub Desktop
Haz clic en el siguiente enlace [GitHub Desktop](https://github.com/apps/desktop) selecciona el sistema operativo de tu preferencia

## Creación de entornos virtuales
The module used to create and manage virtual environments is called venv. venv will install the Python version from which the command was run (as reported by the --version option). For instance, executing the command with python3.12 will install version 3.12.

Para crear un entorno virtual, decide en que carpeta quieres crearlo y ejecuta el módulo venv como script con la ruta a la carpeta:

```sh
python -m venv tutorial-env
```
Esto creará el directorio tutorial-env si no existe, y también creará directorios dentro de él que contienen una copia del intérprete de Python y varios archivos de soporte.

Una ruta común para el directorio de un entorno virtual es .venv. Ese nombre mantiene el directorio típicamente escondido en la consola y fuera de vista mientras le da un nombre que explica cuál es el motivo de su existencia. También permite que no haya conflicto con los ficheros de definición de variables de entorno .env que algunas herramientas soportan.

Una vez creado el entorno virtual, podrás activarlo.

En Windows, ejecuta:
```sh
tutorial-env\Scripts\activate
```

En Unix o MacOS, ejecuta:
```sh
source tutorial-env/bin/activate
```
(Este script está escrito para la consola bash. Si usas las consolas csh or fish, hay scripts alternativos activate.csh y activate.fish que deberá usar en su lugar.)

Activar el entorno virtual cambiará el prompt de tu consola para mostrar que entorno virtual está usando, y modificará el entorno para que al ejecutar python sea con esa versión e instalación en particular. Por ejemplo:
```py
$ source ~/envs/tutorial-env/bin/activate

(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```
Para desactivar el entorno virtual, digita:
```sh
deactivate
```
en el terminal.
