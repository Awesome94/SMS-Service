data = {
    "Bankapl v1": "Welcome to the SMS service /v1 general api schema",
    "properties": {
        "register": [
            {"POST": "/v1/register/"},
            {
                "name": "yourname",
                "password": "yourpassword"
            }
        ],
        "login": [{
            "POST": "/v1/login"
        },
            {
                "name": "yourname",
                "password": "yourpassword"
            },
        ],
        "logout": {
            "POST": "/v1/logout"
        },
        "sendsms": [
            {
                "POST": "/v1/sendsms"
            },
            {
                "to_number": "+25678****",
                "message": "Your message comes here"
            }
        ],
    }
}
