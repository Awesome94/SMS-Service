from app import app, nexmo_client, africas_talking_client
from flask import jsonify, request, make_response


@app.route('/', methods=['GET'])
def load_home_page():
    return jsonify({
        "message": "welcome to The sms service"
    }), 200


@app.route('/v1/send_sms', methods=['POST'])
def send_sms():
    client = ''
    sms_data = request.json
    q_object = {
        "to_number": sms_data.get('to_number'),
        "message": sms_data.get('message'),
        "sender": sms_data.get('sender'),
        "provider": sms_data.get('provider')
    }

    reciever = sms_data.get('to_number')
    message = sms_data.get('message')
    provider = sms_data.get('provider')

    if provider == 'nexmo':
        client = nexmo_client
    elif provider == 'a_stalking':
        client = africas_talking_client
    else:
        client = africas_talking_client

    response = client.send(reciever, message, q_object)
    return make_response(jsonify(response))
