from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.BooleanField()


class Projects(models.Model):
    ids = models.IntegerField(primary_key=True, verbose_name='项目主键', help_text='项目主键')

    name = models.CharField(max_length=20, verbose_name='项目名称', help_text='项目名称',
                            unique=True)
    leader = models.CharField(max_length=10, verbose_name='项目负责人', help_text='项目负责人')

    is_execute = models.BooleanField(verbose_name='是否启动项目', help_text='是否启动项目',
                                     default=True)

    desc = models.TextField(verbose_name='项目描述', help_text='项目描述', null=True,
                            blank=True, default='')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')

    class Meta:
        db_table = 'tb_projects'