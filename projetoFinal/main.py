from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import pywhatkit

# inicializando o wikipedia em portugues
wikipedia.set_lang("pt")
# inicializando a engine de reconhecimento de audio
engine = pyttsx3.init()
# inciiando o reconhecimento de voz
voz = engine.getProperty("voices")

engine.setProperty("voice", voz)
engine.setProperty("language", "pt-br")

ativadorVoz = "lisa"  # para ativar deve uma palavra simples

# configurando um navegador para brir
edgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edgePath))


def fale(text, rate=160):
    
    """Função que transforma texto em voz
    Args:
        text (string): Texto que foi dito durante o parseCommand
        rate (int, optional): Velocidade da fala. Defaults to 120.
    """
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()


def paraTexto():
    
    """Comando que transforma voz em texto

    Returns:
        string: Texto que foi dito durante a verificação
    """
    
    listener = sr.Recognizer()
    print("Ouvindo seu pedido")

    with sr.Microphone() as source:
        listener.pause_threshold = 1
        input_speech = listener.listen(source)

    try:
        print("Identificando seu pedido")
        vozParaTexto = listener.recognize_google(input_speech, language="pt_br")
        print(f"O seu pedido é: {vozParaTexto}")
    except Exception as exception:
        print("Não entendi oque você falou, poderia repetir?")
        fale("Não entendi oque você falou, poderia repetir?")
        print(exception)
        return "None"

    return vozParaTexto

def pesquisarWikipedia(vozParaTexto):
    procurarResultados = wikipedia.search(vozParaTexto)
    if not procurarResultados:
        print('Sem resultados')
        return 'Não houve resultados encontrados'
    try:
        pagWiki = wikipedia.page(procurarResultados[0])
    except wikipedia.DisambiguationError as error:
        pagWiki = wikipedia.page(error.options[0])
    print(pagWiki.title)
    resumoWiki = str(pagWiki.summary)
    return resumoWiki
          
# Loop Main

if __name__ == "__main__":
    fale("Ligada.")

    while True:
        # transformando o comando em split.
        vozParaTexto = paraTexto().lower().split()
        
        if vozParaTexto[0] == ativadorVoz:
            vozParaTexto.pop(0)

            # Comandos
            if vozParaTexto[0] == "diga":
                if "oi" in vozParaTexto:
                    fale("Olá, tudo bem? Sou a inteligencia artificial feita pela NEON")
                else:
                    vozParaTexto.pop(0)  #Tira o "diga"
                    speech = " ".join(vozParaTexto)
                    fale(speech)

            #comando para abrir o navegador      
            if vozParaTexto[0] == "abra" and vozParaTexto[1] == "o" and vozParaTexto[2] == 'site':
                fale("Abrindo...")
                vozParaTexto = " ".join(vozParaTexto[3:])
                webbrowser.get('edge').open_new(vozParaTexto)
                
            #Wikipedia
            
            if vozParaTexto[0] == "pesquise" and vozParaTexto[1] == 'sobre' :
                vozParaTexto = ' '.join(vozParaTexto[2:])
                fale('Pesquisando no wikipedia')
                fale(pesquisarWikipedia(vozParaTexto))

            #Anotar
            if vozParaTexto[0] == "anotar":
                fale("Já peguei o papel e caneta")
                notaNova = paraTexto().lower()
                agora = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
                with open ('note_%s.txt' % agora, 'w') as newFile:
                    newFile.write(notaNova)
                fale("Anotado!")                
                
            #Educação né amigo
            if vozParaTexto[0] == "obrigado":
                vozParaTexto = ' '.join(vozParaTexto[1:])
                fale("Não há de quê")
                
            #sair
            if vozParaTexto[0]== "sair":
                fale("Até mais!")
                break

            if vozParaTexto[0]=="buscar":
                pesquisa = vozParaTexto[1:]
                pywhatkit.playonyt(pesquisa)
                

                
               