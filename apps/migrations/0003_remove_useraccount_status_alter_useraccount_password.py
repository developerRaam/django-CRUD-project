# Generated by Django 4.1.4 on 2022-12-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_useraccount_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='status',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='password',
            field=models.CharField(editable=False, max_length=250),
        ),
    ]
