from app import app
from app.helpers import SMS, NexmoSMS, response, token_required
from flask import jsonify, request, make_response
from app.models import User
from app.data import data

africas_talking_client = SMS()
nexmo_client = NexmoSMS()


@app.route('/', methods=['GET'])
def load_home_page():
    return jsonify({
        "v1": data
    }), 200


@app.route('/v1/register', methods=['POST'])
def register():
    # query if the user exists
    user = User.query.filter_by(name=request.json.get('name')).first()

    if not user:
        try:
            post_data = request.json
            # register the user
            name = post_data.get('name')
            password = post_data.get('password')
            user = User(name=name, password=password)
            user.save()
            return response('success', 'account created', 201)

        except Exception as e:
            # In case of any errors, return a String message containing the error
            result = {
                'message': str(e)
            }
            return make_response(jsonify(result)), 401
    else:
        # User is Already in the database so we do not want to register them twice
        return response('Already exists', 'Please Login', 202)


@app.route('/v1/login', methods=['POST'])
def login_user():
    try:
        # Get the user object using their email
        user = User.query.filter_by(
            name=request.json.get('name')).first()

        # Try to authenticate the found user using their password
        if user and user.password_is_valid(request.json.get('password')):
            # Generate the access token. This will be used as the authorization header

            access_token = user.generate_token(user.id)

            if access_token:
                print(access_token)
                response = {
                    'message': 'You logged in successfully.',
                    'access_token': access_token.decode()
                }
                return make_response(jsonify(response)), 200
        else:
            # User does not exist. so error message
            response = {
                'message': 'Invalid email or password, Please try again'
            }
            return make_response(jsonify(response)), 401

    except Exception as e:
        # Create a response containing an string error message
        response = {
            'message': str(e)
        }
        # Return a server error using the HTTP Error Code 500 (Internal Server Error)
        return make_response(jsonify(response)), 500


@app.route('/v1/logout', methods=['POST'])
def log_out(self):
    return "logout successful"


@app.route('/v1/sendsms', methods=['POST'])
@token_required
def send_sms(self):
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
        client = nexmo_client

    response = client.send(q_object)
    return make_response(jsonify(response))
