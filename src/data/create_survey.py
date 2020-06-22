import boto3
import os


def get_table():
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    return table


# This will run in the Lambda environment and be reused across invocations
default_table = get_table()


def create_survey(survey=None, table=default_table):
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
