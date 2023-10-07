from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_student = models.BooleanField('Is student', default=False)
    is_staff = models.BooleanField('Is staff', default=False)
    is_editor = models.BooleanField('Is editor', default=False)

