from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):

    name: models.CharField
    slug: models.SlugField
    description: models.TextField
    created_at: models.DateTimeField
    updated_at: models.DateTimeField
    is_active: models.BooleanField


    name = models.CharField(max_length=50, unique=True,null=False)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active  = models.BooleanField(default=True)

    def save(self, *args, **kwargs)-> None:
        self._set_slug()
        super().save(*args, **kwargs)
    
    def _set_slug(self)-> None:
        if not self.slug:
            self.slug = slugify(self.name)

    def __str__(self) -> str:
        return self.name
     




class Visibility (models.TextChoices):
    PUBLIC = 'PUB', 'Public'
    PRIVATE  = 'PRI', 'Private'
    ARCHIVED = 'ARC', 'Archived'


class Exercise (models.Model):
    name: models.CharField
    slug: models.SlugField
    description: models.TextField
    created_by: models.ForeignKey
    category:  models.ForeignKey
    created_at: models.DateTimeField
    updated_at : models.DateTimeField
    visibility: models.CharField

    name = models.CharField(max_length=80, unique=True,null=False)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(null=False)
    created_by = models.ForeignKey(
                                    to=User, 
                                    on_delete=models.CASCADE, 
                                    related_name='exercises'
                                  )
    category  = models.ForeignKey(
                                    to=Category, 
                                    on_delete=models.CASCADE, 
                                    related_name='exercises'
                                 )
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    visibility = models.CharField(
                                    choices=Visibility, 
                                    null=False, 
                                    default=Visibility.ARCHIVED
                                 )

    def save(self, *args , **kwargs)-> None:
        self._set_slug()
        super().save(*args, **kwargs)

    def _set_slug(self)-> None:
        if not self.slug:
            self.slug = slugify(self.name)

    def __str__(self)-> str:
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercises'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
            models.Index(fields=['created_by']),
            models.Index(fields=['category'])
        ]
