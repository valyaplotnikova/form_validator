import logging
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tinydb import TinyDB


logger = logging.basicConfig(level=logging.INFO, filemode='w', filename='py.log', format='%(levelname)s | %(message)s')

db = TinyDB('database.json')


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


@csrf_exempt
def get_form(request):
    logger.info(f"Request method: {request.method}")
    logger.info(f"Request body: {request.body}")
    if request.method == 'POST':
        form_data = request.POST.dict()
        logger.info(f"Form data: {form_data}")
        templates = db.all()

        for template in templates:
            template_fields = {k: v for k, v in template.items() if k != 'name'}
            if all(field in form_data and determine_field_type(form_data[field]) == field_type
                   for field, field_type in template_fields.items()):
                return JsonResponse({"form_name": template["name"]})

        # Если подходящая форма не найдена, вернуть типы полей
        field_types = {field: determine_field_type(value) for field, value in form_data.items()}
        return JsonResponse(field_types)


