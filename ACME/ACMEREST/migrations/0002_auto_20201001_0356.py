# Generated by Django 3.1.1 on 2020-10-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACMEREST', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='id',
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
