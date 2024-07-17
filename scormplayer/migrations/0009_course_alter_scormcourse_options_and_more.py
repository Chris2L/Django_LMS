# Generated by Django 4.2.7 on 2024-03-12 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scormplayer", "0008_rename_course_scormcourse"),
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
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "verbose_name": "Course",
                "verbose_name_plural": "Courses",
            },
        ),
        migrations.AlterModelOptions(
            name="scormcourse",
            options={
                "verbose_name": "ScormCourse",
                "verbose_name_plural": "ScormCourses",
            },
        ),
        migrations.RemoveField(
            model_name="scormcourse",
            name="id",
        ),
        migrations.RemoveField(
            model_name="scormcourse",
            name="name",
        ),
        migrations.AddField(
            model_name="scormcourse",
            name="course_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="scormplayer.course",
            ),
            preserve_default=False,
        ),
    ]