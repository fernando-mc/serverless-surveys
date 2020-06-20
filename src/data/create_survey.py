import os

def get_table():
    import boto3
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])

    return dynamodb, table

dynamodb, table = get_table()


def create_survey(survey=None):
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
