from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from django.conf import settings
# Create your models here.


def cover_upload_to(instance, filename):
    return f'bookcover/{filename}'

def book_upload_to(instance, filename):
    return f'books/{filename}'

class BookManager(models.Manager):
    def get_queryset(self):
        return super(BookManager, self).get_queryset().filter(is_available=True)
    
    


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=225)
    
    class Meta:
        verbose_name_plural = "Authors"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name
    
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=225, null=True)
    website_url = models.URLField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Publishers"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("publisher_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name



class Genre(models.Model):
    name = models.CharField(max_length=100,)
    slug = models.SlugField(max_length=225, unique=True, null=True)
    
    class Meta:
        verbose_name_plural = "Genres"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("gnere_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='books')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    detail = models.TextField()
    slug = models.SlugField(max_length=225, unique=True, null=True)
    cover_img_url = models.ImageField(upload_to=cover_upload_to, height_field=None, width_field=None, max_length=None)
    book_url = models.FileField(upload_to=book_upload_to, max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    books = BookManager()
    
    
    @property
    def total_rating(self):
        return self.reviews.all().count()
    
    @property
    def average_rating(self):
        return self.reviews.all().aggregate(models.Avg('rating')).get('rating__avg')
    
    class Meta:
        verbose_name_plural = "Books"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
    
    
