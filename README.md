# Wifi
aplicación web para auditar redes de forma automatizada con linux

Aviso de Seguridad
Esta herramienta es solo para fines educativos. Úsela solo en redes que sean de su propiedad o tenga permiso explícito para probar.

# Instalar dependencias de python:
pip install flask

# Abrir la aplicacion mediante Flask:
python app.py

# Asegurate de tener instalado las siguientes herramientas:
# - aircrack-ng
# - airodump-ng
# - aireplay-ng
# - iwconfig
# - hping3

# Note: Esta aplicacion requiere ser ejecutado con privilegios.
# RUN: sudo python app.py o sudo flask run
# Note2: Para crackear la contraseña se debe de tener rockyou en :/home/kali/Downloads/

Requisitos Previos:
Sistema Operativo Kali Linux
Python 3.x
Paquetes necesarios:
  Flask
  Suite aircrack-ng
  hping3 (para ataques DDoS)

Instalación:
Instalar paquetes Python requeridos:
pip install flask

Instalar herramientas de Kali Linux necesarias:
Instalar suite aircrack-ng y hping3:
sudo apt install aircrack-ng hping3

Uso:
Clonar el repositorio
Navegar al directorio del proyecto
Ejecutar la aplicación con privilegios de root:
sudo python app.py
Abrir un navegador web y navegar a:
http://localhost:5000

Características
Listar interfaces inalámbricas
Activar/desactivar modo monitor
Escanear redes inalámbricas
Capturar handshakes WPA
Realizar ataques de desautenticación
Realizar ataques DDoS
Crackeo de contraseñas usando diccionario rockyou

