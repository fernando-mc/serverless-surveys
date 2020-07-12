import boto3
import os
from src.entities.responses import response_from_item


def get_table():
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    return table


# This will run in the Lambda environment and be reused across invocations
default_table = get_table()


def get_response(response=None, table=default_table):
    try:
        item = table.get_item(
            Key=response.key()
        )['Item']
        response = response_from_item(item)
        return response
    except Exception as e:
        print("Error getting response")
        print(e)
        error_message = "Could not get response"
        return {
            "error": error_message
        }

