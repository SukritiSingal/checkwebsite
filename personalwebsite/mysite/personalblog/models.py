from django.db import models

# Create your models here.
class pblog(models.Model):
	ID= models.IntegerField(primary_key=True)
	Title = models.CharField(max_length=50)
	Content = models.TextField()
    