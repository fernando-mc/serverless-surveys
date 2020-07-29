import boto3
import os
from boto3.dynamodb.conditions import Key
from src.entities.responses import response_from_item


def get_table():
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    return table


# This will run in the Lambda environment and be reused across invocations
default_table = get_table()


def get_all_survey_responses(survey=None, table=default_table):
    try:
        pk = Key("PK").eq(survey.sk())
        sk = Key("SK").begins_with("RESPONSE#")
        expression = pk & sk
        result = table.query(
            KeyConditionExpression=expression
        )
        if not result.get("Items"):
            return {"responses": []}
        responses = []
        for item in result["Items"]:
            responses.append(response_from_item(item))
        return responses
    except Exception as e:
        print("Error getting survey responses")
        print(e)
        error_message = "Could not get survey responses"
        return {
            "error": error_message
        }
