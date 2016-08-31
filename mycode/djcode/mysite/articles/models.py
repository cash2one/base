from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Classes(models.Model):
	name = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length = 50)
	author = models.CharField(max_length = 30)
	about = models.CharField(max_length= 100)
	pub_date = models.DateField() 
	content = RichTextField('articles')       
	classes = models.ForeignKey(Classes)

	def __unicode__(self):
		return self.title        




