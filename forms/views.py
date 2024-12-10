from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from tinydb import TinyDB

from forms.utils import determine_field_type, get_request_data


db = TinyDB('forms/database.json')


@csrf_exempt
def get_form(request):
    return render(request, "index.html")


def form_answer(request):
    form_data = get_request_data(request.POST.get('request'))
    templates = db.all()

    for template in templates:
        template_fields = {k: v for k, v in template.items() if k != 'name'}

        if all(field in form_data and determine_field_type(form_data[field]) == field_type
               for field, field_type in template_fields.items()):
            return JsonResponse({"form_name": template["name"]})

    field_types = {field: determine_field_type(value) for field, value in form_data.items()}

    return JsonResponse(field_types)
