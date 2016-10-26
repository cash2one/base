from django.contrib import admin
from restaurants.models import Restaurant, Food,Comment, Test
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Comment)
admin.site.register(Test)
