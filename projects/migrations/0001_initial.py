# Generated by Django 4.1.4 on 2023-01-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键')),
                ('name', models.CharField(help_text='项目名称', max_length=20, unique=True, verbose_name='项目名称')),
                ('leader', models.CharField(help_text='项目负责人', max_length=10, verbose_name='项目负责人')),
                ('is_excute', models.BooleanField(default=True, help_text='是否启动项目', verbose_name='是否启动项目')),
                ('desc', models.TextField(blank=True, default='', help_text='项目描述信息', null=True, verbose_name='项目描述信息')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '项目表',
                'verbose_name_plural': '项目',
                'db_table': 'tb_projects',
                'ordering': ['id'],
            },
        ),
    ]