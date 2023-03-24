import speech_recognition as sr
from openAI import openAI
from esperaSalida import esperaSalida

grabador = sr.Recognizer()
grabador.energy_threshold = 4000 # Umbral de cancelacion de ruido

def app () :
    continuar = menu()
    while continuar == True:
        Grabacion()
        print("\n")
        continuar = esperaSalida()

def Grabacion():
    with sr.Microphone() as source:
        print("\n# Preparate")
        grabador.adjust_for_ambient_noise(source) # Calibrando microfono
        print("# Escuchando tu peticion...") 
        audioGrabado = grabador.listen(source) # Esta grabando

    try:
        print("# Reconociendo la peticion...\n")
        text = grabador.recognize_google(audioGrabado, language="es-AR")
        print("-Vos: " + text)
        openAI(text)
    except Exception as ex:
        print("No reconoci ninguna palabra clara")

def menu():
    entrada = input('Presione ENTER para comenzar ')
    return entrada == ''

app()