# Generated by Django 3.0.7 on 2020-06-16 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_remove_observation_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation_individual',
            name='client_race',
            field=models.ManyToManyField(help_text='Hold down "Control", or "Command" on a Mac, to select more than one.', to='survey.Race'),
        ),
    ]
