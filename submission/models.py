from django.contrib.auth.models import User
from django.db import models

from language.models import ExerciseLanguage

# Create your models here.


class Verdict(models.TextChoices):
    ACCEPTED = "AC", "Accepted"
    WRONG_ANSWER = "WA", "Wrong Answer"
    TIME_LIMIT_EXCEEDED = "TLE", "Time Limit Exceeded"
    MEMORY_LIMIT_EXCEEDED = "MLE", "Memory Limit Exceeded"
    RUNTIME_ERROR = "RE", "Runtime Error"
    COMPILATION_ERROR = "CE", "Compilation Error"
    NOT_EVALUATED = "NE", "Not Evaluated"



class Submission(models.Model):
    score             : models.IntegerField
    exercise_languge  : models.ForeignKey
    submited_at       : models.DateTimeField
    output            : models.TextField
    time_used         : models.FloatField
    memory_used       : models.IntegerField
    veredict          : models.CharField
    user              : models.ForeignKey
    
    exercise_languge = models.ForeignKey(
                                        ExerciseLanguage,
                                        blank = False,
                                        null=  False,
                                        on_delete=models.CASCADE
                                        )
    score = models.IntegerField(blank=False, null=False)
    submited_at = models.DateTimeField(blank= False, null=False, auto_now_add=True)
    output = models.TextField(blank=False, null=False)
    time_used = models.FloatField(blank=False, null=False)
    memory_used = models.IntegerField(blank=False, null=False)
    user =  models.ForeignKey(
                            User,
                            blank = False,
                            null=  False,
                            on_delete=models.CASCADE
                            )
    veredict = models.CharField(blank = False, 
                                null=False, 
                                choices=Verdict, 
                                default=Verdict.NOT_EVALUATED)

    class Meta:
        ordering = ['-submited_at']
        indexes = [
            models.Index(fields=['time_used']),
            models.Index(fields=['user']),
            models.Index(fields=['veredict']),
            models.Index(fields=['memory_used'])
        ]

