from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator

from store.models import Book

# Create your models here.


class UserManager(BaseUserManager):
    
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        if not first_name:
            raise ValueError(_('Users must have firstname'))
        if not last_name:
            raise ValueError(_('User must have lastname'))
        if password is None:
            raise ValueError(_('Users must have a Password'))
        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if not extra_fields.get('is_staff'):
            raise ValueError(_('staff must be set to true'))
        if not extra_fields.get('is_superuser'):
            raise ValueError(_('Superuser must be set to true'))
        user = self.create_user(email, first_name, last_name, password, **extra_fields)
        return user
    
    def get_queryset(self):
        return super(UserManager, self).get_queryset().filter(is_active=True)
    
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = UserManager()
    
    def tokens(self):
        '''it will be used for the implementation of jwt for rest api'''
        return ''
    
    def __str__(self):
        return f'{self.first_name}. {self.last_name[0]}'
    
    
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