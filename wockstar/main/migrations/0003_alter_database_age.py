# Generated by Django 3.2.9 on 2021-11-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_database_clientid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
    ]
