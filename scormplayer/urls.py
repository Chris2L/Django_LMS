from django.urls import path

from .views import index, save_scorm, index_2004, save_scorm_2004

urlpatterns = [
    path('scorm/<course_id>/', index, name='scorm'),
    path('scorm/<course_id>/save', save_scorm, name='save_scorm'),
    path('scorm_2004/', index_2004, name='scorm_2004'),
    path('save_scorm_2004/', save_scorm_2004, name='save_scorm_2004'),
]