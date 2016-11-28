#from app import Util
import aiml,sys
from unidecode import unidecode

def formatOutPut(text):

    text = text.replace('\\t','\t')
    text = text.replace('\\n','\n')

    return text

def stripCommand(text):
    if(text[0] == '/'):
        return text[1:]
    return text

def sanitizeMessage(text):
    aux = unidecode(text)
    aux = aux.lower()
    return stripCommand(aux)

def main():

    #create and configurate bot knowledbase
    ctfbot = aiml.Kernel()
    ctfbot.learn("resources/knowledgebase.aiml")

    while True:

        question = stripCommand(input("> "))
        if question == 'quit':
            return 0

        response = ctfbot.respond(sanitizeMessage(question))

 #       print( Util.formatOutPut(response))
        print(formatOutPut(response))



if __name__ == '__main__':
    
    sys.exit(int(main() or 0))