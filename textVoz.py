import pyttsx3

def textVoz(entradaTexto):
    print("-GPT: " + entradaTexto)
    texto = entradaTexto
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') # Obtener todas las voces disponibles

    for voice in voices: # Buscar la voz "Spanish-Latin America" y establecerla como la voz actual
        if 'Spanish-Latin America' in voice.name:
            if voice.languages and voice.languages[0] == u'es-mx':
                engine.setProperty('voice', voice.id)
                break

    engine.setProperty('rate', 170) # Establecer la velocidad de la voz
    engine.say(texto) # Salidad del texto con la voz seleccionada
    engine.runAndWait() # Esperar que termine