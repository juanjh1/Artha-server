from django.contrib.auth.models import AbstractUser
from django.db import models

from rank.models import Rank


class UserModel(AbstractUser):
    id                 : models.IntegerField
    avatar             : models.URLField
    score              : models.IntegerField
    completed_problems : models.IntegerField
    status             : models.BooleanField
    created_at         : models.DateTimeField
    last_active        : models.DateTimeField

    id = models.IntegerField(primary_key=True)
    avatar = models.URLField(blank=True, null=True)
    score = models.IntegerField(default=0)
    completed_problems = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=False, blank=False)

    def __str__(self) -> str:
        return str(self.email)
