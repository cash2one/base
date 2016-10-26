from django.shortcuts import render_to_response
from django.db.models import Q
from books.models import Book
# Create your views here.

def search(request):
	query = request.GET.get('q','')
	if query:
		qset=(
			Q(title__icontains=query) |
			Q(author__first_name__icontains=query) |
			Q(author__last_name__icontains=query) 
		)

		results = Book.objects.filter(qset).distinct()
	else:
		results = []
	
	return render_to_response('search.html',{'results':results,'query':query})


