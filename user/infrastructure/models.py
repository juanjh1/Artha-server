from django.db import models
from rank.models import Rank

class UserModel(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    avatar = models.URLField(blank=True, null=True)
    score = models.IntegerField(default=0)
    completed_problems = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.email