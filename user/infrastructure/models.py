from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import get_object_or_404

from rank.models import Rank


class UserModel(AbstractUser):
    
    avatar             : models.URLField
    score              : models.IntegerField
    completed_problems : models.IntegerField
    rank               : models.ForeignKey

    avatar             = models.URLField(blank=True, null=True)
    score              = models.IntegerField(default=0)
    completed_problems = models.IntegerField(default=0)
    rank               = models.ForeignKey( 
                                            Rank, 
                                            on_delete=models.CASCADE, 
                                            null=True, 
                                            blank=True
                                           )

    def __str__(self) -> str:
        
        return str(self.email)
    
    @staticmethod
    def get_user_by_email(email:str) -> "UserModel":
        
        return get_object_or_404(UserModel,email=email)
    
    @staticmethod
    def get_user_by_username(username:str)-> "UserModel":
        
        return get_object_or_404(UserModel,username=username)
      
    @staticmethod
    def validate_user_identifiers_not_exist(
                                email: str | None = None,\
                                username: str | None = None\
                                ) -> "UserModel" :
        
        from django.http import Http404
        
        try:

            if(email is not None):
            
                return UserModel.get_user_by_email(email)
        
            if(username is not None):
            
                return UserModel.get_user_by_username(username) 
        
        except UserModel.DoesNotExist:
            
            raise Http404('User don\'t exist') 

        raise Http404('Email and username void, try again whit correct values') 
    
    @staticmethod
    def validate_user_existence(email : str | None, username : str | None) -> bool:
        
        email_exist_validation : bool = UserModel.\
                                    objects.\
                                    filter(email = email).exists() 
        
        username_exist_validation : bool = UserModel.\
                                    objects.\
                                    filter(username= username).exists() 

        return (email_exist_validation or  username_exist_validation)
        
    class Meta:
       
        ordering = ['-date_joined']
        
        verbose_name = 'User'
        
        verbose_name_plural = 'Users'
        
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['rank']),
        ]
