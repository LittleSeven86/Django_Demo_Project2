# Generated by Django 4.1.4 on 2023-01-12 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interfaces',
            fields=[
                ('id', models.AutoField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('name', models.CharField(help_text='接口名称', max_length=20, unique=True, verbose_name='接口名称')),
                ('tester', models.CharField(help_text='测试人员', max_length=10, verbose_name='测试人员')),
                ('projects', models.ForeignKey(help_text='所属项目', on_delete=django.db.models.deletion.CASCADE, to='projects.projects', verbose_name='所属项目')),
            ],
            options={
                'verbose_name': '接口表',
                'verbose_name_plural': '接口表',
                'db_table': 'tb_interfaces',
                'ordering': ['id'],
            },
        ),
    ]
