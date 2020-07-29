import boto3


def dev_table():
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table('test-surveys-dev')
    return table
