# Generated by Django 3.0.8 on 2020-12-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0005_auto_20201204_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semana',
            name='tema',
            field=models.CharField(max_length=100),
        ),
    ]