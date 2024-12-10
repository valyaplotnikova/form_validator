import re


def get_request_data(data):
    request_data = data.split('&')
    request_dict = {field: field_type for field, field_type in [data.split('=') for data in request_data]}
    return request_dict


def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None


def validate_phone(phone):
    return re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", phone) is not None


def validate_date(date):
    return re.match(r"^\d{2}\.\d{2}\.\d{4}$", date) is not None or re.match(r"^\d{4}-\d{2}-\d{2}$", date) is not None


def determine_field_type(value):
    if validate_date(value):
        return 'date'
    elif validate_phone(value):
        return 'phone'
    elif validate_email(value):
        return 'email'
    else:
        return 'text'
