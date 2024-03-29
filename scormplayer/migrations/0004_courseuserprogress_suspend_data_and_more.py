# Generated by Django 4.2.7 on 2024-01-26 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scormplayer", "0003_courseuserprogress_exit_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="courseuserprogress",
            name="suspend_data",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="courseuserprogress",
            name="lesson_status",
            field=models.CharField(
                choices=[
                    ("incomplete", "Incomplete"),
                    ("complete", "Complete"),
                    ("completed", "Completed"),
                    ("passed", "Passed"),
                ],
                default="incomplete",
                max_length=10,
            ),
        ),
    ]
