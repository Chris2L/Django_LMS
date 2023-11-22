from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Course(models.Model):

    name = models.CharField(max_length=150)
    # file or path?

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.name

class CourseUserProgress(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # cmi.core.lesson_status varvalue=completed or cmi.core.lesson_status varvalue=failed  or cmi.core.lesson_status varvalue=passed 
    # completion_status
    # success_status
    # scaled cmi.core.score.raw varvalue=53 cmi.core.score.min varvalue=0 mi.core.score.max varvalue=100 
    # session_time cmi.core.session_time varvalue=0000:04:39
    # location
    # exit - suspend or "" to restart cmi.core.exit varvalue= / cmi.core.exit varvalue=suspend 
    

    class Meta:
        verbose_name = _("CourseUserProgress")
        verbose_name_plural = _("CourseUserProgress's")

    def __str__(self):
        return self.name
