from django.shortcuts import render
from .models import Book

def home(request):
    return render(request, 'home.html')

def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query) | books.filter(author__name__icontains=query)

    return render(request, 'library/search.html', {'books': books})
