Request
{
	"to_number":"+256785916689",
	"sender": 5225,
	"message": "this is it man",
	"provider": "nexmo"
}

Response
{
    "message-count": "1",
    "messages": [
        {
            "message-id": "1400000051F4D282",
            "message-price": "0.06090000",
            "network": "64110",
            "remaining-balance": "1.81730000",
            "status": "0",
            "to": "256785916689"
        }
    ]
}

Safcom req
{
	"to_number":"+256785916689",
	"sender": 5225,
	"message": "this is it man",
	"provider": "a_stalking"
}

safcom Res
{
    "SMSMessageData": {
        "Message": "Sent to 1/1 Total Cost: KES 1.0677",
        "Recipients": [
            {
                "cost": "UGX 35.0000",
                "messageId": "ATXid_31a6707378eca2714d38b55c869b2117",
                "number": "+256785916689",
                "status": "Success",
                "statusCode": 101
            }
        ]
    }
}