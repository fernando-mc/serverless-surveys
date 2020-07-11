import pytest
import re
from src.entities.responses import Response, NoSurveyIdException
from tests.utils.regexes import valid_uuid


def test_instantiating_response_class_with_no_data_fails():
    with pytest.raises(NoSurveyIdException):
        Response()


def test_instantiating_response_class_with_valid_data():
    survey_id = '1'
    response_id = '1'
    response_data = {'key': 'value'}
    response = Response(survey_id=survey_id, response_id=response_id, response_data=response_data)

    assert response.survey_id == survey_id
    assert response.response_id == response_id
    assert response.response_data == response_data


def test_instantiating_survey_with_blank_survey_id_uses_uuid_string_fallback():
    survey_id = '1'
    response_data = {'key': 'value'}
    response = Response(survey_id=survey_id, response_data=response_data)

    assert response.survey_id == survey_id
    assert response.response_id is not None
    assert isinstance(response.response_id, str)
    assert valid_uuid(response.response_id)


def test_response_key():
    survey_id = 'TESTSURVEYID'
    response_id = 'TESTRESPONSEID'
    response = Response(
        survey_id=survey_id,
        response_id=response_id,
        response_data=None
    )
    test_key = {
        'PK': 'SURVEY#TESTSURVEYID',
        'SK': 'RESPONSE#TESTRESPONSEID'
    }
    assert isinstance(response.key(), dict)
    assert response.key() == test_key


def test_response_to_item_serialization():
    survey_id = 'TESTSURVEYID'
    response_id = 'TESTRESPONSEID'
    response = Response(
        survey_id=survey_id,
        response_id=response_id,
        response_data={'response': 'data'}
    )
    test_item = {
        'PK': 'SURVEY#TESTSURVEYID',
        'SK': 'RESPONSE#TESTRESPONSEID',
        'survey_id': 'TESTSURVEYID',
        'response_id': 'TESTRESPONSEID',
        'response_data': {'response': 'data'}
    }
    assert isinstance(response.to_item(), dict)
    assert response.to_item() == test_item
