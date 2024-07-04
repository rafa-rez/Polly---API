import json
import random
import string
import os
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['DYNAMODB_CUSTOMER_TABLE']
table = dynamodb.Table(table_name)

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
    while True:
        new_id = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if not id_exists(new_id):
            return new_id

def id_exists(phrase_id):
    try:
        response = table.get_item(Key={'primary_key': phrase_id})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return 'Item' in response

def post(event, context):
    body = json.loads(event.get('body', '{}'))
    
    phrase = body.get('phrase', '')
    
    existing_item = get_item_by_phrase(phrase)
    if existing_item:
        response_body = {
            "id": existing_item['primary_key'],
            "message": f"Phrase already exists in the database.",
            "phrase": existing_item['phrase']
        }

        response = {"statusCode": 200,"body": json.dumps(response_body),"headers": {"Content-Type": "application/json"}}

        return response

    phrase_id = generate_id()

    item = {
        'primary_key': phrase_id,
        'phrase': phrase
    }

    try:
        table.put_item(Item=item)
    except ClientError as e:
        error_message = e.response['Error']['Message']
        print(f"Error saving the phrase: {error_message}")
        response_body = {
            "message": "Error saving the phrase.",
            "error": error_message
        }
        response = {
            "statusCode": 500,
            "body": json.dumps(response_body),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response

    response_body = {
        "id": phrase_id,
        "message": f"Received phrase: {phrase}"
    }

    response = {"statusCode": 200,"body": json.dumps(response_body),"headers": {"Content-Type": "application/json"}}

    return response

def get_item_by_phrase(phrase):
    try:
        response = table.scan(FilterExpression='phrase = :p',ExpressionAttributeValues={':p': phrase})
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None
    else:
        items = response.get('Items', [])
        if items:
            return items[0]
        else:
            return None
