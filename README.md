Crochet Detector Bot 🧶🤖

Descripción

Este proyecto consiste en un bot de Discord que utiliza un modelo de inteligencia artificial para analizar imágenes y determinar si un crochet fue hecho por una persona o generado por inteligencia artificial.
El bot recibe imágenes enviadas por los usuarios en un canal de Discord, las procesa utilizando un modelo entrenado con TensorFlow y MobileNetV2, y devuelve una predicción junto con el nivel de confianza del modelo.
Dependiendo de la confianza de la predicción, el bot también indica si está seguro o no del resultado.

¿Cómo funciona?

Un usuario envía una imagen en Discord usando el comando del bot.
El bot guarda la imagen temporalmente en la carpeta images.
La imagen se procesa con el modelo entrenado (best_moodpet_model.h5).
El modelo clasifica la imagen en una de dos clases:
- Crochet → Crochet hecho por una persona
- CrochetIA → Crochet generado por inteligencia artificial

El bot devuelve un mensaje con la predicción y el porcentaje de confianza.
Si la confianza es menor a 70%, el bot indica que no está seguro de la clasificación.

Tecnologías utilizadas
- Python
- Discord.py
- TensorFlow / Keras
- MobileNetV2
- NumPy
- PIL (Python Imaging Library)

Archivos
- bot.py : Contiene el bot de Discord y los comandos que permiten recibir imágenes y enviar la predicción.
- model.py : Carga el modelo entrenado y contiene la función que procesa las imágenes y realiza la clasificación.

Ejemplos del funcionamiento

Aquí se pueden ver algunos ejemplos del bot funcionando en Discord.
![Ejemplo 1](https://drive.google.com/file/d/1d_xCeHqTxgeTtHVNwd-GNMTmf4Rb_XPa/view?usp=sharing)
![Ejemplo 2](https://drive.google.com/file/d/1qYKyYoXe8RBCw3ei1L1tFfBWqOx6KYZp/view?usp=sharing)

Modelo de clasificación

El modelo fue entrenado utilizando MobileNetV2, una arquitectura de redes neuronales convolucionales optimizada para clasificación de imágenes.
El modelo fue entrenado para distinguir entre:
- Crochet real
- Crochet generado por inteligencia artificial

Las imágenes se redimensionan a 224x224 píxeles antes de ser procesadas por el modelo.

Licencia

Este proyecto se distribuye bajo la licencia MIT.
Puedes usar, modificar y distribuir este código libremente, siempre que se mantenga el aviso de copyright original.
