# Generated by Django 2.0.3 on 2018-03-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature_request_app', '0002_feature_requests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature_requests',
            name='target_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
