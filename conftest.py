import os

import boto3
import pytest

from moto import mock_dynamodb2

os.environ['DYNAMODB_TABLE'] = 'surveys'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

# Consider replacing this with moto3's mock_sts
@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'


@pytest.fixture(scope='function')
def dynamodb(aws_credentials):
    with mock_dynamodb2():
        yield boto3.resource('dynamodb', region_name='us-east-1')


@pytest.fixture(scope='function')
def dynamodb_table(dynamodb):
    """Create a DynamoDB surveys table fixture."""
    table = dynamodb.create_table(
        TableName='surveys',
        KeySchema=[
            {
                'AttributeName': 'PK',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'SK',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'PK',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'SK',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName='surveys')
    yield
