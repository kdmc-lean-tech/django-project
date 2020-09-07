import json


def errorMessage(message):
    error = {
        'message': message
    }
    return json.dumps(error)


def sendMessage(message):
    mess = {
        'message': message
    }
    return json.dumps(mess)

