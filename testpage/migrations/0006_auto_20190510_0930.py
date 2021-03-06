# Generated by Django 2.2.1 on 2019-05-10 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testpage', '0005_auto_20190509_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='frist_name',
            field=models.CharField(help_text='输入姓名', max_length=30, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, help_text='输入签名', max_length=240, null=True, verbose_name='签名'),
        ),
        migrations.AlterField(
            model_name='person',
            name='size_name',
            field=models.CharField(choices=[('m', '数学'), ('c', '语文'), ('e', '英语')], default='m', help_text='选择科目', max_length=1, verbose_name='科目'),
        ),
        migrations.CreateModel(
            name='interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_name', models.CharField(help_text='请输入兴趣名', max_length=10, verbose_name='兴趣的名字')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testpage.Person')),
            ],
        ),
    ]
