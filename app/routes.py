from app import app, nexmo_client, africas_talking_client
from flask.views import View
from flask import Flask, jsonify, request, make_response
import nexmo


@app.route('/v1/send_sms', methods=['POST'])
def send_sms():
    sms_data = request.json

    to_number = sms_data.get('to_number')
    message = sms_data.get('message')
    sender = sms_data.get('sender')

    nexmo_client.send_message({
        'from': sender,
        'to': to_number,
        'text': message

    })
    africas_talking_client(to_number, message, sender)