from django.urls import path

from .views import index, save_scorm

urlpatterns = [
    path('', index, name='home'),
    path('save_scorm/', save_scorm, name='save_scorm'),
]