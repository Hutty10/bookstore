from django.shortcuts import render
import random

from .models import Book

# Create your views here.

def home(request):
    count = Book.objects.all().count()
    if count >= 3:
        _slice = random.random() * (count - 3)
    _slice = random.random() * (count - count)
    features = Book.books.all()[_slice: _slice+3]
    bestsellers = Book.books.all()[:8]
    return render(request, 'index.html', {'features':features,'bestsellers':bestsellers})

def books(request):
    data = Book.books.all()
    return render(request, 'store/ebooks.html', {'books':data})
