from django.db import models

# Create your models here.


class Publisher(models.Model):
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=150)
	city = models.CharField(max_length=50)
	sate_province = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	website = models.URLField()
	
	# ...
	def __unicode__(self):
		return self.name
		
class Author(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField()
	
	# ..
	def __unicode__(self):
		return u"%s.%s" % (self.first_name,self.last_name)

class Book(models.Model):
	title = models.CharField(max_length=20)
	author =models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	pub_date = models.DateField()

	# ...
	def __unicode__(self):
		return self.title	

