from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/')
