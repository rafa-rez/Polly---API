import json
import random
import string

def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        #"input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v1_description(event, context):
    body = {
        "message": "TTS api version 1."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def generate_id(length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def post(event, context):
    body = json.loads(event.get('body', '{}'))
    
    phrase = body.get('phrase', '')
    phrase_id = generate_id()

    response_body = {
        "id": phrase_id,
        "message": f"Received phrase: {phrase}"
    }

    response = {"statusCode": 200, "body": json.dumps(response_body), "headers": {"Content-Type": "application/json"}}

    return response
