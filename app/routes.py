from app import app, nexmo_client
from flask.views import View
from flask import Flask, jsonify, request, make_response
import nexmo

client = nexmo.Client(key='', secret='')
client.send_message({
    'from': 'Nexmo',
    'to': ' ',
    'text': ' '

})


@app.route('/v1/send_sms', methods=['POST'])
def send_sms(self):
    to_number = ''
    message = ''
    nexmo_client.send_message({
        'from': 'Nexmo',
        'to': to_number,
        'text': message

    })
