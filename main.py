import speech_recognition as sr
import openai

# Crear un objeto de reconocimiento de voz
grabacion = sr.Recognizer()
grabacion.energy_threshold = 4000


def app () :
    opcion = menu()
    while opcion == "1":
        Recording(1,4)
        print("\n\n")
        opcion = menu()

def menu():
    opc = input("# 1-Charlar\n# 2-Salir\n# Opcion: ")
    return opc

####################################################################################

def OPENAI(pregunta):
    # Establece tu clave de API de OpenAI
    openai.api_key = "api-key"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=pregunta,
        max_tokens=250
    )
    return print("-GPT: " + response.choices[0].text)


def Recording(min, max):
    with sr.Microphone() as source:
        print("\n# Preparate")
        grabacion.adjust_for_ambient_noise(source, duration=min)
        print("# Escuchando tu peticion...")
        recorded_audio = grabacion.listen(source, timeout=max)

    try:
        print("# Reconociendo la peticion...\n")
        text = grabacion.recognize_google(recorded_audio, language="es-ES")
        print("-Vos: " + text)
        OPENAI(text)
    except Exception as ex:
        print("No reconoci ninguna palabra clara")

app()