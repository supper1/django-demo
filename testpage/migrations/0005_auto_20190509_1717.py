# Generated by Django 2.2.1 on 2019-05-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpage', '0004_person_size_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='frist_name',
            field=models.CharField(help_text='第一个名字', max_length=30, verbose_name='name1'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, help_text='第二个名字', max_length=30, null=True, verbose_name='name2'),
        ),
        migrations.AlterField(
            model_name='person',
            name='size_name',
            field=models.CharField(choices=[('s', 'small'), ('m', 'medium'), ('l', 'large')], default='s', help_text='选择尺寸', max_length=1, verbose_name='尺寸'),
        ),
    ]
