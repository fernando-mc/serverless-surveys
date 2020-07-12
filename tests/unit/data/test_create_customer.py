import pytest
from tests.utils.dynamodb import mocked_table


class StubCustomer:

    def __init__(self):
        pass

    def to_item(self):
        return {
            'PK': 'CUSTOMER#TEST_ID',
            'SK': 'PROFILE#TEST_ID',
            'customer_id': 'TEST_ID',
            'profile_data': {'some': 'data'}
        }


def test_create_customer_returns_customer_instance(dynamodb_table):
    from src.data.create_customer import create_customer
    customer_instance = StubCustomer()
    table = mocked_table()
    assert create_customer(
        customer=customer_instance,
        table=table
    ) == customer_instance


def test_create_customer_returns_error_info_when_it_fails(dynamodb_table):
    from src.data.create_customer import (
        create_customer, CustomerCreationException
    )
    table = mocked_table()
    with pytest.raises(CustomerCreationException):
        create_customer(
            customer='Garbage',
            table=table
        )
