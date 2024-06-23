from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
# class users(models.Model):
#     user_name=models.CharField(max_length=100,unique=True)
#     password=models.CharField(max_length=100)