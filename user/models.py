from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from store.models import Book

# Create your models here.
class ReviewManager(models.Manager):
    def get_queryset(self):
        return super(ReviewManager, self).get_queryset().filter(is_active=True)


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    reviews = ReviewManager()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Reviews"
    
    def __str__(self):
        return f'{self.rating} | {self.book} | {self.author}'