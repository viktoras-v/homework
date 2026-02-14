import boto3
import json
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ.get("TABLE_NAME", "Cars-SAM-ua5"))

def getAllCars(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*",
    }
    method = event.get("httpMethod", "POST")
    if method == "GET":
        # Scan all records
        response = table.scan()
        items = response.get("Items", [])
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps(items)
        }
    elif method == "POST":
        payload = json.loads(event["body"])
        import uuid
        table.put_item(Item={
            "Cars_id": "CAR#{}".format(str(uuid.uuid1())),
            "Cars_brand": payload["Cars_brand"],
            "Cars_model": payload["Cars_model"],
            "Cars_year": payload["Cars_year"]
        })
        return {
            "statusCode": 200,
            'headers': headers,
            "body": "OK"
        }
    else:
        return {
            "statusCode": 405,
            "headers": headers,
            "body": "Method Not Allowed"
        }