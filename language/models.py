from django.db import models

from exercise.models import Exercise


class Language(models.Model):
    name: models.CharField
    exercises: models.ManyToManyField

    name = models.CharField(max_length=50, unique=True, null=False)
    exercises = models.ManyToManyField(Exercise, through="ExerciseLanguage")


class MemoryLimit (models.IntegerChoices):
    LOW     = 64 , "Low"
    MEDIUM  = 128, "Medium"
    HIGH    = 512, "High"


class TimeLimit (models.IntegerChoices):
    LOW     = 100, "Low"
    MEDIUM  = 200, "Medium"
    HIGH    = 500, "High"


class ExerciseLanguage(models.Model):
    exercise: models.ForeignKey
    language: models.ForeignKey
    preloaded: models.TextField
    inital_solution: models.TextField
    test_cases: models.TextField
    test_example_case: models.TextField
    created_at: models.DateTimeField
    updated_at: models.DateTimeField
    timeout: models.IntegerField
    memory_limit: models.IntegerField


    exercise = models.ForeignKey(   
                                    to=Exercise, 
                                    on_delete=models.CASCADE,
                                    related_name="exercise_language" )
    language = models.ForeignKey(
                                to=Language,
                                on_delete=models.CASCADE,
                                related_name="exercise_language"
                                )
    preloaded = models.TextField(null=False)
    test_cases = models.TextField(null=False)
    test_example_case = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True)
    timeout = models.IntegerField(
                                    choices=TimeLimit,
                                    default=TimeLimit.LOW
                                 )
    ## memory_limit = mb <- importannntttt
    memory_limit = models.IntegerField(
                                        choices= MemoryLimit,
                                        default= MemoryLimit.LOW
                                      )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["exercise", "language"], 
                name="unique_language_exercise"
            )
        ]