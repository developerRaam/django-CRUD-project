# Generated by Django 4.1.4 on 2022-12-28 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_remove_useraccount_status_alter_useraccount_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentmaster',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.useraccount'),
        ),
        migrations.AddField(
            model_name='subincidenttype',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.useraccount'),
        ),
        migrations.AlterField(
            model_name='subincidenttype',
            name='indicdent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.incidentmaster'),
        ),
    ]
