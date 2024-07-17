# Generated by Django 4.2.7 on 2023-11-30 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
            ],
            options={
                "verbose_name": "Course",
                "verbose_name_plural": "Courses",
            },
        ),
        migrations.CreateModel(
            name="CourseInteraction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
            ],
            options={
                "verbose_name": "CourseInteraction",
                "verbose_name_plural": "CourseInteractions",
            },
        ),
        migrations.CreateModel(
            name="CourseObjective",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField()),
                ("name", models.CharField(max_length=150)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scormplayer.course",
                    ),
                ),
            ],
            options={
                "verbose_name": "CourseObjective",
                "verbose_name_plural": "CourseObjectives",
            },
        ),
        migrations.CreateModel(
            name="Score",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("min", models.FloatField()),
                ("max", models.FloatField()),
                ("raw", models.FloatField()),
                ("scaled", models.FloatField()),
            ],
            options={
                "verbose_name": "Score",
                "verbose_name_plural": "Scores",
            },
        ),
        migrations.CreateModel(
            name="CourseUserProgress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lesson_location", models.IntegerField(default=0)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scormplayer.course",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "CourseUserProgress",
                "verbose_name_plural": "CourseUserProgress's",
            },
        ),
        migrations.CreateModel(
            name="CourseUserObjective",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course_objective",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scormplayer.courseobjective",
                    ),
                ),
                (
                    "course_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scormplayer.courseuserprogress",
                    ),
                ),
                (
                    "score",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scormplayer.score",
                    ),
                ),
            ],
            options={
                "verbose_name": "CourseUserObjective",
                "verbose_name_plural": "CourseUserObjectives",
            },
        ),
        migrations.CreateModel(
            name="CourseUserInteraction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("learner_response", models.CharField(max_length=300)),
                (
                    "result",
                    models.CharField(
                        choices=[("incorrect", "Incorrect"), ("correct", "Correct")],
                        max_length=300,
                    ),
                ),
                ("weighting", models.FloatField()),
                (
                    "course_interaction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scormplayer.courseinteraction",
                    ),
                ),
                (
                    "course_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scormplayer.courseuserprogress",
                    ),
                ),
            ],
            options={
                "verbose_name": "CourseInteraction",
                "verbose_name_plural": "CourseInteractions",
            },
        ),
        migrations.AddField(
            model_name="courseinteraction",
            name="course_objectives",
            field=models.ManyToManyField(to="scormplayer.courseobjective"),
        ),
    ]