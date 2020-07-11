import boto3
import os
from src.entities.customers import customer_from_item


def get_table():
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    return table


# This will run in the Lambda environment and be reused across invocations
default_table = get_table()


def get_customer(customer=None, table=default_table):
    try:
        response = table.get_item(
            Key=customer.key()
        )
        item = response['Item']
        customer = customer_from_item(item)
        return customer
    except Exception as e:
        print("Error getting customer")
        print(e)
        error_message = "Could not get customer"
        return {
            "error": error_message
        }

