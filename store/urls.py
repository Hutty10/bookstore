from django.urls import path, include
from .views import home, books


app_name = 'store'

urlpatterns =[
    path('', home, name='home'),
    path('books/', books, name='books')
]