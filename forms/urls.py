from django.urls import path

from .apps import FormsConfig
from .views import get_form


app_name = FormsConfig.name

urlpatterns = [
    path('get_form/', get_form, name='get_form'),
]
