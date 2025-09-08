from django.db import models

from artha.settings import MAX_SCORE, MIN_SCORE

# Create your models here.


class Rank(models.Model):
    name         : models.CharField
    color        : models.SmallIntegerField
    description  : models.TextField
    position     : models.IntegerField
    min_score    : models.SmallIntegerField
    max_score    : models.SmallIntegerField
    created_at   : models.DateTimeField
    updated_at   : models.DateTimeField
    
    name        = models.CharField(max_length=40, null=False, unique=True)
    position    = models.IntegerField(unique=True)
    description = models.TextField(null=False, blank=False)
    min_score   = models.SmallIntegerField(null=False, blank=False, default=MIN_SCORE)
    max_score   = models.SmallIntegerField(null=False, blank=False, default=MAX_SCORE)
    color       = models.SmallIntegerField(blank=False, null=False)
    created_at  = models.DateTimeField(null=False, blank= False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    
