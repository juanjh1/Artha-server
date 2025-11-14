from typing import Any

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from rank.infrastructure.models import Rank


class Category(models.Model):
    name: models.CharField
    slug: models.SlugField
    user: models.ForeignKey
    description: models.TextField
    created_at: models.DateTimeField
    updated_at: models.DateTimeField
    is_active: models.BooleanField


    name = models.CharField(max_length=50, unique=True,null=False)
    slug = models.SlugField(unique=True, blank=True, null= False)
    description = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    is_active  = models.BooleanField(default=True)
    user = models.ForeignKey(
                             User, 
                             on_delete=models.CASCADE,
                             null= False, 
                             blank=False
                            )
    

    def save(self, *args: Any, **kwargs:Any)-> None:
        self._set_slug()
        super().save(*args, **kwargs)
    
    def _set_slug(self)-> None:
        if not self.slug:
            self.slug = slugify(str(self.name))

    def __str__(self) -> str:
        return str(self.name)  


class Visibility (models.TextChoices):
    PUBLIC = 'PUB', 'Public'
    PRIVATE  = 'PRI', 'Private'
    ARCHIVED = 'ARC', 'Archived'


class Exercise (models.Model):
    name        : models.CharField
    slug        : models.SlugField
    user        : models.ForeignKey
    description : models.TextField
    category    : models.ForeignKey
    created_at  : models.DateTimeField
    updated_at  : models.DateTimeField
    visibility  : models.CharField
    rank        : models.ForeignKey
    

    name = models.CharField(max_length=80, unique=True,null=False)
    slug = models.SlugField(unique=True, blank=False, null=False)
    description = models.TextField(null=False)
    category  = models.ForeignKey(
                                    to=Category, 
                                    on_delete=models.CASCADE, 
                                    related_name='exercises'
                                 )
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    visibility = models.CharField(
                                    choices=Visibility, 
                                    null=False, 
                                    default=Visibility.ARCHIVED
                                 )
    
    user = models.ForeignKey(
                             User, 
                             on_delete=models.CASCADE,
                             null= False, 
                             blank=False
                            )
    
    rank = models.ForeignKey(
                             Rank,
                             on_delete= models.CASCADE,
                             null= False,
                             blank= False
                             )

    def save(self, *args:Any, **kwargs: Any)-> None:
        self._set_slug()
        super().save(*args, **kwargs)

    def _set_slug(self)-> None:
        if not self.slug:
            self.slug = slugify(self.name)

    def __str__(self)-> str:
        return str(self.name)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercises'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
            models.Index(fields=['user']),
            models.Index(fields=['category'])
        ]
    
