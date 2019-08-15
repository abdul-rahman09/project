# Generated by Django 2.2.3 on 2019-08-15 16:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jsonModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jsonmodel',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='jsonmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
