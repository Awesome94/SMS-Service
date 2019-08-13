## SMS-Service
A service that sends SMS to different service providers.
- Trello Board => <https://trello.com/b/4JSVnajx/sms-service>
## Overview
This is a simple SMS service (RestApi) for sending sms' with the following options:

-   Choose a provider of your choice.
-   Choose to Use default provider(Nexmo) by not specifying a particular provider.

HTTP |End Point  | Result
--- | --- | ----------
`GET` | `/` | `Home/Initial route`.
`POST` | `/register` | `Registers a new user`.
`POSt` | `/login` | `logs in and assigns user a token to access the different endpoints`.
`POST` | `/v1/sendsms` | `Send an sms using a provider of your choice.`
`POST` | `/logout` | `Ends current user session`.

## Installation

 ## Requirements:

* Python 3.6
* pip
* virtualenv

## Run application on Local
1. clone repo. 
    - `$ git clone git@github.com:Awesome94/SMS-Service.git`

    - `$ cd SMS-Service/`

2. Create and activate a virtual environment and install requirements:

    - `$ mkvirtualenv <name_of_your_choice>`

    - `$ pip install -r requirements.txt.`

3.  create a local database initiate, run migrations and upgrade db:
    - `$ export FLASK_APP=app/__init__.py`
    - `$ createdb smsservice`
    - `$ flask db init`
    - `$ flask db upgrade`

4. Start your application

    `$ python run run.py`
```
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader
```
You can now open the API with Curl from the command line:
or Postman.(The choice is yours)


You can also access the landing endpont directly in your browser, by opening <http://127.0.0.1:5000/>

## Running tests.
- `$ pytest`

## Nexmo provider(Request).

```
{
	"to_number":"+25678*****",
	"message": "Testing Sms service with Nexmo",
	"provider": "nexmo"
}
```
### Response.
```
{
    "message-count": "1",
    "messages": [
        {
            "message-id": "1400000051F4D282",
            "message-price": "0.06090000",
            "network": "64110",
            "remaining-balance": "1.81730000",
            "status": "0",
            "to": "+25678*****"
        }
    ]
}
```

## Africastalking provider(Request).
```
{
	"to_number":"+25678*****",
	"message": "Testing africa'stalking as provider",
	"provider": "astalking"
}
```

### Response.

```
{
    "SMSMessageData": {
        "Message": "Sent to 1/1 Total Cost: KES 1.0677",
        "Recipients": [
            {
                "cost": "UGX 35.0000",
                "messageId": "ATXid_31a6707378eca2714d38b55c869b2117",
                "number": "+25678*****",
                "status": "Success",
                "statusCode": 101
            }
        ]
    }
}
```