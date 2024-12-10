from django.urls import path

from .apps import FormsConfig
from .views import get_form, form_answer

app_name = FormsConfig.name

urlpatterns = [
    path('', get_form, name='get_form'),
    path('form_answer/', form_answer, name='form_answer'),

]
