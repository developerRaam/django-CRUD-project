# Generated by Django 4.1.4 on 2022-12-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_incidentmaster_user_id_subincidenttype_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentmaster',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
