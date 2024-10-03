# Proyecto un Blog con reflex
## indice
- [Proyecto un Blog con reflex](#proyecto-un-blog-con-reflex)
  - [indice](#indice)
  - [Iniciar proyecto](#iniciar-proyecto)
  - [Estructura del proyecto](#estructura-del-proyecto)
## Iniciar proyecto
1. crear y acceder a la carpeta del proyecto
```bash
mkdir reflex-blog
cd reflex-blog
```
2. Establecer version de python en el proyecto
```bash
pyenv local 3.12.4
```
3. crear un entorno virtual y activarlo
```bash
python -m venv venv
```
4. instalar dependencias al proyecto
```bash
pip install -r requirements.txt
```
5. iniciar proyecto reflex
```bash
reflex init
```
6. ejercutar proyecto -- este primer comando no solo lazara nuestro proyecto si no que instalara y la primera vez que se ejecute los paquete necesario para correrlo en este proceso tambien se compila por lo que sule demorar un poco.
```bash
reflex run
```
## Estructura del proyecto
- `.web` - esta carpeta sera donde se compile nuestro proyecto reflex en javascript. reflex convertira todo nuestro codigo python que realizemos en reflex y lo compilara a codigo javascript para que sea posible la ejecucion en un navegador web.
- `assets` - es la carpeta donde almacenaremos todos los recursos que nuestre web necesite como imagenes, iconos, estilo, generalmente son recuros estaticos que seran publicos.
- `venv` - es la carpeta que ejecuta nuestro entorno virtual de python este nombre varia segun el nombre que le pongamos a nuestro entorno virtual en el paso 3.
- `reflex_blog` - es la carpeta principal del proyecto es donde trabajaremos el codigo de nuestro proyecto. El nombre de este proyecto sera el nombre que se genere segun el nombre de su carpeta contenedora.
  - `reflex_blog.py` - es el archivo de entra de nuestro proyecto el `entrypoint` que se ejecutara una ves se inicialize el proyecto reflex, en este archivo sera donde condifiquemos y agregemos nuestro componentes, estilo, etc de reflex.
- `.gitignore` - es el archivo que nos permite listar los archivos que no deseamos que sean seguido por git estos no seran subidos a nuestro github
- `requirements.txt` - es el archivo que tendra las dependencias que usa de nuestro proyecto.
- `rxconfig.py` - archivo con las configuracion generales que tendra nuestro proyecto