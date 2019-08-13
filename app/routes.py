from app import app, nexmo_client, africas_talking_client
from flask.views import View
from flask import Flask, jsonify, request, make_response


@app.route('/v1/send_sms', methods=['POST'])
def send_sms():
    sms_data = request.json

    to_number = sms_data.get('to_number')
    message = sms_data.get('message')
    sender = sms_data.get('sender')
    provider = sms_data.get('provider')

    if provider == 'nexmo':
        client = nexmo_client
    elif provider == 'a_stalking':
        client = africas_talking_client
    elif provider == '':
        client = africas_talking_client

    client.send(to_number, message, sender)
