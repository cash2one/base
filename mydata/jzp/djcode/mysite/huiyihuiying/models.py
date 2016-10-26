#coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
from django_thumbs.db.models import ImageWithThumbsField
# Create your models here.

class Channel(models.Model):
	fid = models.ForeignKey('self',blank=True,null=True,verbose_name="上级栏目",help_text="不选代表的是顶级栏目")
	name = models.CharField(max_length=30,verbose_name="栏目名称")
    	sort = models.SmallIntegerField(verbose_name="排序",help_text="从小到大排列",default=50)
    	def __unicode__(self):
        	return self.name
    	class Meta:
        	verbose_name = '栏目管理'
        	verbose_name_plural = '栏目管理'


class Article(models.Model):
	title = models.CharField(max_length=60,verbose_name='标题')
    	channel = models.ForeignKey(Channel,verbose_name='所属栏目')
    	keywords = models.CharField(max_length=80,verbose_name='关键字')
    	description = models.CharField(max_length=200,verbose_name='栏目描述')
    	author = models.CharField(max_length=30,blank=True,verbose_name='作者')
    	date = models.DateField(verbose_name = '发布时间')
	#    image = ImageWithThumbsField(blank=True,verbose_name=u'缩略图',upload_to='uploads')
	image1 = ImageWithThumbsField(blank=True,verbose_name=u'网站缩略图',upload_to='uploads')
    	click = models.IntegerField(default=0,verbose_name='点击次数')
    	content = RichTextField(verbose_name = '文档内容')
    	def __unicode__(self):
        	return u'%s %s' % (self.title,self.channel)
    	class Meta:
        	ordering = ['-id']
        	verbose_name_plural = '文档管理'

