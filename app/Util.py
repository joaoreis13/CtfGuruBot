from flask import current_app as app
import requests,json,uuid

def formatOutPut(text):

    text = text.replace('\\t','\t')
    text = text.replace('\\n','\n')

    return text

def stripCommand(text):
    if(text[0] == '/'):
        return text[1:]
    return text

def reportUnknownSentence(text):

    msg = {

    'id' : str(uuid.uuid4()),
    'to' : app.config['REPORT_CONTACT'],
    'type': 'text/plain',
    'content' : text
    }

    hdr = {
    'Authorization':'key '+ app.config['BLIP_KEY']
    }

    if app.config['DEBUG']:
        print("[REPORT]:")
        print(msg)
        print(hdr)

    sent = requests.post(app.config['MSG_URL'],json=msg,headers=hdr)

    if app.config['DEBUG']:
        print(sent)