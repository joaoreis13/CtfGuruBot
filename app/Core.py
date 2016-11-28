from flask import current_app as app
from . import Util
import requests,json,uuid

"""
    Core.processMessage(content )

    Receive a json with the content of a request in the
    Blip API format.
"""
def processMessage(content,bot):

    msgType = content['type']
    msgText = Util.sanitizeMessage( content['content'] )
    msgFrom = content['from']
    session = msgFrom.split('@')[0]

    #process the message to get the awnser
    if msgType == 'text/plain':

        text = Util.formatOutPut( bot.respond(msgText,session) )
    
    else:
        text = "Foi mal champz, não entendo esse tipo de mídia ainda. Manda uma msg ai!"

    #check if the message is an error message and send report to selected user
    if text[0] == "#":
        Util.reportUnknownSentence(msgText)
        text = text[1:]

    msg = {

        'id' : str(uuid.uuid4()),
        'to' : content['from'],
        'type': 'text/plain',
        'content' : text
    }

    hdr = {
        'Authorization':'key '+ app.config['BLIP_KEY']
    }

    if app.config['DEBUG']:
        print("Sending:")
        print(msg)
        print(hdr)

    sent = requests.post(app.config['MSG_URL'],json=msg,headers=hdr)

    if app.config['DEBUG']:
        print(sent)