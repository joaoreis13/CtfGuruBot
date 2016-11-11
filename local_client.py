from app import Util
import aiml,sys


def main():

    #create and configurate bot knowledbase
    ctfbot = aiml.Kernel()
    ctfbot.learn("aiml/knowledgebase.aiml")

    while True:

        question = input("> ")
        if question == 'quit':
            return 0

        response = ctfbot.respond(question)

        print( Util.formatOutPut(response))



if __name__ == '__main__':
    
    sys.exit(int(main() or 0))