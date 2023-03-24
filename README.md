# Charlando con chatGPT: Procesamiento por voz <img src="https://storage.googleapis.com/replit/images/1674608855465_996234acf8be071c053213c4767a8816.jpeg" alt="Alt Text" width="50" height="50"> <img src="https://previews.123rf.com/images/virtaa/virtaa1511/virtaa151100009/48180609-icono-de-sonido-s%C3%ADmbolo-de-altavoz-vector-volumen-el-estilo-de-dise%C3%B1o-plano-moderno-m%C3%ADnimo.jpg" alt="Alt Text" width="50" height="50">

##### Este proyecto utiliza la librería SpeechRecognition de Python para permitir a los usuarios interactuar con ChatGPT de una manera más natural, a través de la voz. Además, también utiliza la API de OpenAI para generar respuestas inteligentes y conversacionales.

## Cómo funciona
##### El programa utiliza la librería SpeechRecognition para capturar la entrada de audio del micrófono. Luego, utiliza la función recognize_google() de la librería para convertir la entrada de voz en texto utilizando la API de Google Speech Recognition.
##### A continuación, el texto se envía al modelo de lenguaje ChatGP, el mismo procesa el pedido y devuelve una respuesta en forma de texto.
##### Finalmente, el texto se convierte en voz utilizando la librería pyttsx3, la cual utiliza una síntesis de voz para convertir el texto en voz y leerlo en voz alta.
##### El proceso se repite hasta que el usuario decide salir del programa.

## Requisitos
### Antes de ejecutar este programa, se deben instalar las siguientes librerías de Python:
    openAI: para el uso de herramientas de openAI como "text-davinci-003"
    pyAudio: para la captura de voz a través del micrófono.
    SpeechRecognition: para la conversión de voz a texto.
    pyttsx3: para la conversión de texto a voz.

### Estas librerías se debe configurar e instalar usando el administrador de paquetes de Python pip, con los siguientes comandos:

### - En terminal instalar lo siguiente:
##### `pip install openai`
##### `pip install PyAudio`
##### `pip install SpeechRecognition`
##### `pip install pyttsx3`
### - Ejecutar el programa:
##### `python ./main.py`

### - En codigo:
#### Configurar tu API-KEY con tu propia api-key.
![image](https://user-images.githubusercontent.com/69114833/226231121-aff69469-793d-4812-9d3b-66dd26602f3b.png)
###### Puedes encontrarla en https://platform.openai.com/account/api-keys

## Ejemplo:
![image](https://user-images.githubusercontent.com/69114833/227566907-749b121f-fe1e-4c31-94a8-1afbf4454a14.png)