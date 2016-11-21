def formatOutPut(text):

    text = text.replace('\\t','\t')
    text = text.replace('\\n','\n')

    return text

def stripCommand(text):
    if(text[0] == '/'):
        return text[1:]
    return text