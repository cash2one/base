from django.contrib import admin
from books.models import Publisher, Author, Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
	list_display=('title','publisher','pub_date')
	search_fields=('title',)

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book,BookAdmin)
