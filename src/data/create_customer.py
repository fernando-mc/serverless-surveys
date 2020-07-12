import boto3
import os


class CustomerCreationException(Exception):
    pass


def get_table():
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])
    return table


# This will run in the Lambda environment and be reused across invocations
default_table = get_table()


def create_customer(customer=None, table=default_table):
    try:
        table.put_item(
            Item=customer.to_item()
        )
        return customer
    except Exception as e:
        print("Error creating customer")
        print(e)
        error_message = "Could not create customer"
        raise CustomerCreationException(error_message)
