# Projeto simples de reconhecimento de voz em inglês


from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# inicializando a engine de reconhecimento de audio
engine = pyttsx3.init()
# inciiando o reconhecimento de voz
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)  # 0= homem, 1=mulher
activationWord = "computer"  # para ativar deve uma palavra simples


def speak(text, rate=120):
    """Função que transforma texto em voz
    Args:
        text (string): Texto que foi dito durante o parseCommand
        rate (int, optional): Velocidade da fala. Defaults to 120.
    """
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()


def parseCommand():
    """Comando que transforma voz em texto

    Returns:
        string: Texto que foi dito durante a verificaçao documentação
    """
    listener = sr.Recognizer()
    print("Ouvindo seu pedido")

    with sr.Microphone() as source:
        listener.pause_threshold = 1
        input_speech = listener.listen(source)

    try:
        print("Reconhecendo sua voz..........")
        query = listener.recognize_google(input_speech, language="pt_br")
        print(f"O texto falado foi: {query}")
    except Exception as exception:
        print("Não entendi sua burrice, fale de novo")
        print(exception)
        return "None"
    return query


# main

if __name__ == "__main__":
    speak("On", 120)

    while True:
        # transformar em lista
        query = parseCommand().split()

        if query[0] == activationWord:
            query.pop(0)

            # comando da lista
            if query[0] == "say":
                if "Hello" in query:
                    speak("Hi!")
                else:
                    query.pop(0)  # tira diz
                    speech = "  ".join(query)
                    speak(speech)
