# Generated by Django 4.2.7 on 2024-01-31 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scormplayer", "0006_alter_courseuserinteraction_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="name",
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
