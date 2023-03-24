import openai
from textVoz import textVoz

def openAI(pregunta):
    # Establece tu clave de API de OpenAI
    openai.api_key = ""

    response = openai.Completion.create(
        engine="text-davinci-003", # Motor de lenguaje 
        prompt=pregunta, 
        max_tokens=120 # Establece el maximo de tokens que imprime
    )

    return textVoz(response.choices[0].text)