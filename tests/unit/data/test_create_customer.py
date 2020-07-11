from tests.utils.dynamodb import mocked_table

class StubCustomer:

    def __init__(self):
        pass
    
    def to_item(self):
        return {
            'PK': 'CUSTOMER#TESTID',
            'SK': 'PROFILE#TESTID',
            'customer_id': 'TESTID',
            'profile_data': {'some':'data'}
        }


def test_create_customer(dynamodb_table):
    from src.data.create_customer import create_customer
    customer_instance = StubCustomer()
    table = mocked_table()
    assert create_customer(customer=customer_instance, table=table) == customer_instance
