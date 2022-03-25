from django.shortcuts import render
from .models import Book

# Create your views here.

def home(request):
    data = Book.books.all()
    return render(request, 'index.html', {'books':data})

def books(request):
    data = Book.books.all()
    return render(request, 'store/ebooks.html', {'books':data})