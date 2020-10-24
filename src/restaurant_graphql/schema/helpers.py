import json
from graphene.utils.str_converters import to_camel_case
from .types.base import ErrorType


def get_errors(form_errors):
    errors = []
    for field, field_messages in form_errors.items():
        messages = []
        json_error = None
        for message in field_messages:
            try:
                json_error = json.loads(message)
            except json.decoder.JSONDecodeError:
                messages.append(message)

        child_errors = []
        if json_error:
            child_errors = []
            for f, m in json_error.items():
                m = [i['message'] for i in m]
                f = to_camel_case(f) if f != '__all__' else f
                child_errors.append(ErrorType(field=f, messages=m))
        child_errors = child_errors if child_errors else None
        messages = messages if messages else None
        field = to_camel_case(field) if field != '__all__' else field
        errors.append(
            ErrorType(field=field, messages=messages, errors=child_errors)
        )

    return errors
