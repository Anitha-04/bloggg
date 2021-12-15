from django.db import models

class Postblog(models.Model):
    date=models.DateField()
    blog=models.CharField(max_length=1000)
