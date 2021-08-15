# Generated by Django 3.2.5 on 2021-08-14 20:53

from django.db import migrations, models
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210812_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='code_inn',
            field=models.CharField(default='', max_length=12, validators=[main.utils.validate_inn], verbose_name='Tax Code'),
        ),
    ]