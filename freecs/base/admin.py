from django.contrib import admin
from .models import Member
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Member)