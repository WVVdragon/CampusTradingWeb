# Generated by Django 2.2.6 on 2020-09-30 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0006_delete_commodity'),
    ]

    operations = [
        migrations.CreateModel(
            name='commodity',
            fields=[
                ('commodityID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('transactionType', models.CharField(max_length=10)),
            ],
        ),
    ]
