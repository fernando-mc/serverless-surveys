from src.handlers.create_survey import handler


class Context:
    pass


def test_create_survey_handler_has_cors_handlers():
    print(handler({'body': 'stuff'}, Context))
