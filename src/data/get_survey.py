import boto3
import os
from src.entities.surveys import survey_from_item


def get_table():
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    return table


# This will run in the Lambda environment and be reused across invocations
default_table = get_table()


def get_survey(survey=None, table=default_table):
    try:
        item = table.get_item(
            Key=survey.key()
        )['Item']
        survey = survey_from_item(item)
        return survey
    except Exception as e:
        print("Error getting survey")
        print(e)
        error_message = "Could not get survey"
        return {
            "error": error_message
        }
