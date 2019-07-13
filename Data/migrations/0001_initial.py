# Generated by Django 2.2.3 on 2019-07-12 16:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Route', '0003_auto_20190712_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Route.Route')),
            ],
        ),
    ]
