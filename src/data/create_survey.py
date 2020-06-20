import boto3
import os

def get_table():
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    return table

table = get_table()


def create_survey(survey=None):
    table = get_table()
    try:
        table.put_item(
            Item=survey.to_item()
        )
        return survey
    except Exception as e:
        print("Error creating survey")
        print(e)
        error_message = "Could not create survey"
        return {
            "error": error_message
        }
