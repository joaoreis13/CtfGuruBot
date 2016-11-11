from flask import Flask,request
from . import Core,Endpoint
import requests, json, aiml,os

#creating flask application object
application = Flask(__name__)
BOT_API_ROOT = os.path.join( application.root_path ,'..')

print("Starting bot on " + BOT_API_ROOT)
print("Load config file")
#import config values
application.config.from_object('config')

print("Load config environment variables")
#import environment config variables
application.config['BLIP_KEY'] = os.getenv("BLIP_KEY",application.config['BLIP_KEY'])
application.config['KBFILE'] = os.getenv("KBFILE",application.config['KBFILE'])
application.config['DEBUG'] = os.getenv("DEBUG",application.config['DEBUG'])
if(application.config['DEBUG']):
    print("BLIP_KEY = "+application.config['BLIP_KEY'])
    print("MSG_URL = "+application.config['MSG_URL'])
    print("NOT_URL = "+application.config['NOT_URL'])
    print("CMD_URL = "+application.config['CMD_URL'])
    print("KBFILE = "+application.config['KBFILE'])
    print("DEBUG = "+application.config['DEBUG'])

print("Starting AIML Kernel on Bot")
bot = aiml.Kernel()

print("Loading brain from: ",os.path.join( BOT_API_ROOT , application.config['KBFILE'] ))
bot.learn( os.path.join( BOT_API_ROOT , application.config['KBFILE'] ) )


@application.route('/message',methods=['POST'])
def receiveMessage():

    content = request.get_json()
    Core.processMessage(content,bot)
    return Endpoint.recieveMessage(content)

@application.route('/notification',methods=['POST'])
def receiveNotification():

    return Endpoint.recieveNotification(request.get_json())