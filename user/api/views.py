from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from store.models import Book
from ..models import Review
from .serializers import RegisterSerializer, ReviewSerializer

class RegisterView(GenericAPIView):
    
    serializer_class = RegisterSerializer
    
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        
        return Response(user_data, status=status.HTTP_201_CREATED)
    
    
class CreateReview(CreateAPIView):
        
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()   
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        book = Book.books.get(pk=pk)
        author = self.request.user
        review_queryset = Review.objects.filter(author=author, book=book)
        
        if review_queyset.exists():
            raise ValidationError('You have already reviwed this movie!')
        
        serializer.save(book=book, author=author)
        
        
class ReviewList(ListAPIView):
    
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        book = self.kwargs.get('pk')
        return Review.reviews.filter(book=book)
    

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer