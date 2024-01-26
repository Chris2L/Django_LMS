from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class ResultChoices(models.TextChoices):
    INCORRECT = "incorrect", _("Incorrect")
    CORRECT = "correct", _("Correct")

class LessonStatusChoices(models.TextChoices):
    INCOMPLETE = "incomplete", _("Incomplete")
    COMPLETE = "complete", _("Complete")
    COMPLETED = "completed", _("Completed")
    PASSED = "passed", _("Passed")

class ExitStatusChoices(models.TextChoices):
    SUSPEND = "suspend", _("Suspend")
    RESTART = "", _("Restart")

class CourseFormatChoices(models.IntegerChoices):
    SCORM_12 = 0, _('SCORM 1.2')
    SCORM_2004 = 1, _('SCORM 2004')

class Course(models.Model):
    name = models.CharField(max_length=150)
    format = models.IntegerField(choices=CourseFormatChoices.choices, default=CourseFormatChoices.SCORM_12)
    index = models.FileField(upload_to=None, max_length = 200)

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return f"{self.name} ({self.format})"
    
class Score(models.Model):
    min    = models.FloatField(default=0.0)
    max    = models.FloatField(default=0.0)
    raw    = models.FloatField(default=0.0)
    scaled = models.FloatField(default=1.0)

    class Meta:
        verbose_name = _("Score")
        verbose_name_plural = _("Scores")

    def __str__(self):
        return f"{self.raw:.2f}% -> {self.raw:.2f}/{self.max:.2f}"
    
class CourseObjective(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = _("CourseObjective")
        verbose_name_plural = _("CourseObjectives")

    def __str__(self):
        return f"{self.course} - obj {self.number} -> {self.name}"
    
class CourseInteraction(models.Model):
    # An interaction can have more than one objective
    course_objectives = models.ManyToManyField(CourseObjective)
    name = models.CharField(max_length=150)
    

    class Meta:
        verbose_name = _("CourseInteraction")
        verbose_name_plural = _("CourseInteractions")

    def __str__(self):
        return self.name

class CourseUserProgress(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    lesson_location = models.IntegerField(default=0)

    lesson_status = models.CharField(max_length=10, choices=LessonStatusChoices.choices, default=LessonStatusChoices.INCOMPLETE)
    exit_status = models.CharField(max_length=10, choices=ExitStatusChoices.choices, default=ExitStatusChoices.RESTART)

    score = models.ForeignKey(Score, on_delete=models.CASCADE, null=True)

    # session_time

        #   'lesson_location': 3,
        #   'total_time': '01:17:45.05',
        #   'student_id': "chris2",
        #   'student_name': "Christo Labuschange",
        #   'lesson_status': 'incomplete', # completed passed incomplete
        #   'score': json.dumps({
        #             "raw": '70',
        #             "min": '0',
        #             "max": '100'
        #             }),

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
        return f"{self.course} ({self.user}) @ {self.lesson_location}"
    
class CourseUserObjective(models.Model):
    course_user = models.ForeignKey(CourseUserProgress, on_delete=models.CASCADE)
    course_objective = models.ForeignKey(CourseObjective, on_delete=models.CASCADE)
    score = models.ForeignKey(Score, on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("CourseUserObjective")
        verbose_name_plural = _("CourseUserObjectives")

    def __str__(self):
        return f"{self.course_user} {self.course_objective} {self.score}" 

    
class CourseUserInteraction(models.Model):
    # An interaction can have more than one objective
    course_user = models.ForeignKey(CourseUserProgress, on_delete=models.CASCADE)
    course_interaction = models.ForeignKey(CourseInteraction, on_delete=models.CASCADE)
    
    learner_response = models.CharField(max_length=300)

    result = models.CharField(max_length=50, choices=ResultChoices.choices,)
    weighting = models.FloatField()
    
    class Meta:
        verbose_name = _("CourseInteraction")
        verbose_name_plural = _("CourseInteractions")

    def __str__(self):
        return self.course_user + " " + self.course_interaction