# Generated by Django 4.1.4 on 2022-12-28 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_alter_incidentmaster_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subincidenttype',
            old_name='indicdent_id',
            new_name='indcident_id',
        ),
    ]