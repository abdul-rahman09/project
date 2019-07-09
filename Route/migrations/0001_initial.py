# Generated by Django 2.2.3 on 2019-07-07 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=200)),
                ('bill', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('petrol', models.IntegerField()),
                ('income_tax', models.IntegerField()),
                ('pra', models.IntegerField()),
                ('total_expense', models.IntegerField()),
                ('income', models.IntegerField()),
                ('cheque', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
