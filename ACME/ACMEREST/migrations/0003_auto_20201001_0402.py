# Generated by Django 3.1.1 on 2020-10-01 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ACMEREST', '0002_auto_20201001_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codes',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ACMEREST.empresa'),
        ),
    ]
