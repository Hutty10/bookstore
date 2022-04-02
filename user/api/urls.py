from django.urls import path, include

from .views import RegisterView, CreateReview

urlpatterns =[
    path('register/', RegisterView.as_view(), name='register'),
    path('review/create/<int:pk>', CreateReview.as_view(), name='create-review')
]