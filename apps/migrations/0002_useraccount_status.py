# Generated by Django 4.1.4 on 2022-12-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], default='Deactive', max_length=10),
        ),
    ]
