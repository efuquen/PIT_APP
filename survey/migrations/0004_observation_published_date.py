# Generated by Django 3.0.7 on 2020-06-16 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20200618_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
