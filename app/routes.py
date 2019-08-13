from app import app
from app.helpers import SMS, NexmoSMS
from flask import jsonify, request, make_response

africas_talking_client = SMS()
nexmo_client = NexmoSMS()


@app.route('/', methods=['GET'])
def load_home_page():
    return jsonify({
        "message": "welcome to The sms service"
    }), 200


@app.route('/v1/sendsms', methods=['POST'])
def send_sms():
    client = ''
    sms_data = request.json
    q_object = {
        "to_number": sms_data.get('to_number'),
        "message": sms_data.get('message'),
        "sender": sms_data.get('sender'),
        "provider": sms_data.get('provider')
    }

    provider = sms_data.get('provider')

    if provider == 'nexmo':
        client = nexmo_client
    elif provider == 'astalking':
        client = africas_talking_client
    else:
        client = africas_talking_client

    response = client.send(q_object)
    return make_response(jsonify(response))
