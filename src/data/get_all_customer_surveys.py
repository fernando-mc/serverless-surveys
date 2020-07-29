import boto3
import os
from boto3.dynamodb.conditions import Key
from src.entities.surveys import survey_from_item


def get_table():
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    return table


# This will run in the Lambda environment and be reused across invocations
default_table = get_table()


def get_all_customer_surveys(customer=None, table=default_table):
    try:
        pk = Key("PK").eq(customer.pk())
        sk = Key("SK").begins_with("SURVEY#")
        expression = pk & sk
        result = table.query(
            KeyConditionExpression=expression
        )
        if not result.get("Items"):
            return {"surveys": []}
        surveys = []
        for item in result["Items"]:
            surveys.append(survey_from_item(item))
        return surveys
    except Exception as e:
        print("Error getting customer surveys")
        print(e)
        error_message = "Could not get customer surveys"
        return {
            "error": error_message
        }
