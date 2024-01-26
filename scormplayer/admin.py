from django.contrib import admin

from .models import Course, Score, CourseObjective, CourseInteraction, CourseUserProgress, CourseUserObjective, CourseUserInteraction


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'format', 'index')
    search_fields = ('name',)


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'min', 'max', 'raw', 'scaled')


@admin.register(CourseObjective)
class CourseObjectiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'number', 'name')
    list_filter = ('course',)
    search_fields = ('name',)


@admin.register(CourseInteraction)
class CourseInteractionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    raw_id_fields = ('course_objectives',)
    search_fields = ('name',)


@admin.register(CourseUserProgress)
class CourseUserProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'user', 'lesson_location')
    list_filter = ('course', 'user')


@admin.register(CourseUserObjective)
class CourseUserObjectiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_user', 'course_objective', 'score')
    list_filter = ('course_user', 'course_objective', 'score')


@admin.register(CourseUserInteraction)
class CourseUserInteractionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'course_user',
        'course_interaction',
        'learner_response',
        'result',
        'weighting',
    )
    list_filter = ('course_user', 'course_interaction')