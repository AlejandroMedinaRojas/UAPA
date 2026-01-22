# UAPA

Para poder visualizar la maqueta simulando la landing page debe contar con los siguientes programas
- Python (version 3.8 o mas reciente)
- Git

Una vez cuente con estos programas sencillamente siga los siguientes pasos:
- Cree un entorno virtual en su directorio
- Clone el repositorio
- Instale el framework "reflex" de python usando el comando "pip install reflex"
- Ejecute el comando "reflex run" dentro del directorio donde se encuentra ubicado el archivo "rxconfig.py"
- Visite la pagina "http://localhost:3000" desde un navegador en la maquina donde se esta ejecutando el programa

Trouble shooting

Si el puerto 3000 o el puerto 8000 en su maquina se encuentran ocupados ejecute el comando "reflex run" especificando dos puertos que se escuentren disponibles
e.g. "reflex run --frontend-port 3001 --backend-port 8001"

Debe contar con acceso a Internet ya que el programa utiliza google fonts de manera remota
