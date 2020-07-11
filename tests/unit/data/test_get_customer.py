from tests.utils.dynamodb import mocked_table

class StubCustomer:

    def __init__(self):
        pass
    
    def key(self):
        return {
            'PK': 'CUSTOMER#TESTID',
            'SK': 'PROFILE#TESTID'
        }


def test_get_customer(dynamodb_table):
    from src.data.get_customer import get_customer
    table = mocked_table()
    item = {
        'PK': 'CUSTOMER#TESTID',
        'SK': 'PROFILE#TESTID',
        'customer_id': 'TESTID',
        'profile_data': {'some':'data'}
    }
    table.put_item(Item=item)
    customer_instance = StubCustomer()
    assert get_customer(customer=customer_instance, table=table).to_item() == item
