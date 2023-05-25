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
voz = engine.getProperty("voices")

engine.setProperty("voice", voz)
engine.setProperty("language", "pt-br")
    
ativadorVoz = "lisa"  # para ativar deve uma palavra simples


def falar(text, rate=200):
    """Função que transforma texto em voz
    Args:
        text (string): Texto que foi dito durante o transformarComando
        rate (int, optional): Velocidade da fala. Defaults to 120.
    """
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()


def transformarComando():
    """Comando que transforma voz em texto

    Returns:
        string: Texto que foi dito durante a verificaçao documentação
    """
    listener = sr.Recognizer()
    print('Ouvindo seu pedido')
 
    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)
 
    try: 
        print('Identificando seu pedido')
        vozParaTexto = listener.recognize_google(input_speech, language='pt_br')
        print(f'O seu pedido é: {vozParaTexto}')
    except Exception as exception:
        print('Não entendi oque você falou, poderia repetir?')
        falar('Não entendi oque você falou, poderia repetir?')
        print(exception)
        return 'None'
 
    return vozParaTexto


# main

if __name__ == '__main__':
    falar('Ligada.')

    while True:
        # Parse as a list
        vozParaTexto = transformarComando().lower().split()
        
        if vozParaTexto[0] == ativadorVoz:
            vozParaTexto.pop(0)

            # List commands
            if vozParaTexto[0] == 'diga':
                if 'oi' in vozParaTexto:
                    falar('Olá, tudo bem? Sou a inteligencia artificial feita pela NEON')
                else: 
                    vozParaTexto.pop(0) # Remove say
                    falando = ' '.join(vozParaTexto)
                    falar(falando)
