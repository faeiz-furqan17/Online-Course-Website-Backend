from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
class Member(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email  = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    def __str__(self):
        return self.username.username