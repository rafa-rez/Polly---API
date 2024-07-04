import json


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

def post(event, context):
    body = json.loads(event.get('body', '{}'))
    
    phrase = body.get('phrase', '')

    response_body = {
        "message": f"Received phrase: {phrase}"
    }

    response = {"statusCode": 200,"body": json.dumps(response_body),"headers": {"Content-Type": "application/json"}
    }

    return response
    
