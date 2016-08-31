#coding:utf8
from django.db import models

# Create your models here.


class School(models.Model):
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
	tel = models.CharField(max_length=20)
	email = models.EmailField()

	def __unicode__(self):
		return "%s%s"%(self.name,self.tel)

class Student(models.Model):
	name = models.CharField(max_length=60, verbose_name='姓名')
	age_choice = [x for x in enumerate(range(18,60))]
	age  = models.SmallIntegerField(verbose_name='年龄', choices=age_choice, default='0')
	gender_choice = (('0',u'男'),('1',u'女'))
	gender = models.CharField(max_length=60, choices=gender_choice, verbose_name='性别')
	birth = models.DateField(verbose_name='出生日期', help_text='出生年月日',default='1990-01-01')
	phone = models.CharField(max_length=60, verbose_name='联系方式', help_text='请输入常用手机号码')
	email = models.EmailField(verbose_name='电子邮箱', help_text='请务必输入')
	xl_choice = (('0','大专'),('1','本科'),('2','硕士'),('3','博士'))
	xl    = models.CharField(max_length=60, choices=xl_choice, verbose_name='学历')
	graduatedfrom = models.CharField(max_length=60, verbose_name='毕业院校', help_text='输入您的毕业学校名称')
	marriage_choice = (('0','已婚'),('1','未婚'))
	marriage = models.CharField(max_length=60, choices=marriage_choice, verbose_name='婚姻状态')
	begin_date = models.DateField(verbose_name='入学时间', help_text='何时开始学习',default='2015-07-01')
	courses = models.TextField(max_length=254, verbose_name='学习课程', help_text='多门课程用“|”分开',default=None)
	stay = models.BooleanField(verbose_name='是否住宿', help_text='勾选选择住宿', default=True)
	comefrom_choice = (('0','朋友介绍'),('1','大学渠道'),('2','自己上门'),('3','百度推广'))
	comefrom = models.CharField(max_length=60, choices=comefrom_choice, verbose_name='学员来源',default='大学渠道')
	import_phone = models.CharField(max_length=60, verbose_name='紧急联系人', help_text='亲属或者朋友可用电话')
	introducer = models.ForeignKey('self', blank=True, null=True, verbose_name='介绍人')

	def __unicode__(self):
		return self.name
	class Meta:
        	verbose_name = '学员信息管理'
        	verbose_name_plural = '学员信息管理'

class Grade(models.Model):
	student = models.ForeignKey(Student)
	chinese = models.CharField(max_length=10)
	math = models.CharField(max_length=10)
	english = models.CharField(max_length=10)

#	def __unicode__(self):
#		return self.student


