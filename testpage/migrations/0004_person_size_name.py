# Generated by Django 2.2.1 on 2019-05-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpage', '0003_auto_20190509_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='size_name',
            field=models.CharField(choices=[('s', 'small'), ('m', 'medium'), ('l', 'large')], default='s', max_length=1),
        ),
    ]
