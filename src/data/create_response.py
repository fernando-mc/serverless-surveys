import boto3
import os


def get_table():
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    return table


# This will run in the Lambda environment and be reused across invocations
default_table = get_table()


def create_response(response=None, table=default_table):
    try:
        table.put_item(
            Item=response.to_item()
        )
        return response
    except Exception as e:
        print("Error creating response")
        print(e)
        error_message = "Could not create response"
        return {
            "error": error_message
        }
