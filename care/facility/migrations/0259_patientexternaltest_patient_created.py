# Generated by Django 2.2.11 on 2021-07-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0258_auto_20210623_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientexternaltest',
            name='patient_created',
            field=models.BooleanField(default=False),
        ),
    ]
