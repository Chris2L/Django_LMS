from django.urls import path

from .views import api_get_value, apihtml, index

urlpatterns = [
    path('scorm/', index, name='scorm'),
    path('scorm_api/', apihtml, name='api_html'),
    path('scorm_api/get_value/', api_get_value, name='api_get_value'),
]