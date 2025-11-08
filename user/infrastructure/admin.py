from django.contrib import admin

from user.infrastructure import models

admin.site.register(models.UserModel)
