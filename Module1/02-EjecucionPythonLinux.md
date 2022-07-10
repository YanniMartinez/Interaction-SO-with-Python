# Como ejecutar archivos en Linux

Para ello tenemos 2 alternativas:
1. Llamar al interprete con el comando `python3 hello_world.py`
2. Dando permisos de ejecucuón al archivo con el comando `chmod +x hello_world.py`. Esto sirve sólo sí se especificó la siguiente línea en la línea 1: `#!usr/bin/env python3`. La ejecución sería mediante el comando `./hello_word.py`