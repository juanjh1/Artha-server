from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from artha.settings import MAX_SCORE, MIN_SCORE


class Rank(models.Model):

    name         : models.CharField
    color        : models.CharField
    description  : models.TextField
    position     : models.IntegerField
    min_score    : models.SmallIntegerField
    max_score    : models.SmallIntegerField
    created_at   : models.DateTimeField
    updated_at   : models.DateTimeField
    
    name        = models.CharField(max_length=40, null=False, unique=True)
    position    = models.IntegerField(unique=True)
    description = models.TextField(null=True, blank=False)
    min_score   = models.SmallIntegerField(null=False, blank=False, default=MIN_SCORE)
    max_score   = models.SmallIntegerField(null=False, blank=False, default=MAX_SCORE)
    color       = models.CharField(blank=False, null=False)
    created_at  = models.DateTimeField(null=False, blank= False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    
    
    @staticmethod
    def get_rank_by_name(name: str) -> 'Rank':
        
       return get_object_or_404(Rank, name=name) 
    

    @staticmethod 
    def rank_name_exist(name: str) -> bool:

        return Rank.objects.filter(name=name).exists()
        
    @staticmethod
    def position_exist(pos: int) -> bool:
        
        return Rank.objects.filter(position=pos).exists()

    @staticmethod
    def get_all_ranks()->QuerySet["Rank", "Rank"]:

        return Rank.objects.all()

    class Meta:
       
        ordering = ['-position']
        
        verbose_name = 'Rank'
        
        verbose_name_plural = 'Ranks'
