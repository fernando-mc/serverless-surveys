import pytest
import re
from src.entities.surveys import Survey, NoCustomerIdException


def valid_uuid(uuid):
    regex = re.compile(
        '^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\\Z',  # noqa: E501
        re.I
    )
    match = regex.match(uuid)
    return bool(match)


def test_instantiating_survey_class_with_no_data_fails():
    with pytest.raises(NoCustomerIdException):
        Survey()


def test_instantiating_survey_class_with_valid_data():
    customer_id = '1'
    survey_id = '2'
    survey_data = {'key': 'value'}
    survey = Survey(customer_id, survey_id, survey_data)

    assert survey.customer_id == customer_id
    assert survey.survey_id == survey_id
    assert survey.survey_data == survey_data


def test_instantiating_survey_with_blank_survey_id_uses_uuid_string_fallback():
    customer_id = '1'
    survey_id = None
    survey = Survey(customer_id, survey_id)

    assert survey.customer_id == customer_id
    assert survey.survey_id is not None
    assert isinstance(survey.survey_id, str)
    assert valid_uuid(survey.survey_id)


def test_survey_key():
    customer_id = 'TESTID'
    survey_id = 'TESTID'
    survey = Survey(
        customer_id=customer_id,
        survey_id=survey_id,
        survey_data=None
    )
    test_key = {
        'PK': 'CUSTOMER#TESTID',
        'SK': 'SURVEY#TESTID'
    }
    assert isinstance(survey.key(), dict)
    assert survey.key() == test_key


def test_to_item_serialization():
    customer_id = 'TESTID'
    survey_id = 'TESTID'
    survey = Survey(
        customer_id=customer_id,
        survey_id=survey_id,
        survey_data={'survey': 'data'}
    )
    test_item = {
        'PK': 'CUSTOMER#TESTID',
        'SK': 'SURVEY#TESTID',
        'customer_id': 'TESTID',
        'survey_id': 'TESTID',
        'survey_data': {'survey': 'data'}
    }
    assert isinstance(survey.to_item(), dict)
    assert survey.to_item() == test_item
