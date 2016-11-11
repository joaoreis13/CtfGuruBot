import json
from flask import jsonify

def recieveMessage(content):

    #TODO implement error on delivery and resending in those cases.
    tResp = {'status':'ok'}

    resp = jsonify(tResp)
    resp.status_code = 202
    return resp

def recieveNotification(content):

    #TODO implement error on delivery and resending in those cases.
    #TODO implement ID verification.
    tResp = {'status':'ok'}

    resp = jsonify(tResp)
    resp.status_code = 202
    return resp