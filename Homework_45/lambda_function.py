import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Cars_2')

def lambda_handler(event, context):
    # Parse body
    body = json.loads(event['body'])
    
    # Write to DB
    table.put_item(Item=body)
    
    # Correct reply to Lambda proxy
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'message': 'OK'})
    }
