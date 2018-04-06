from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/')


    def __str__(self):
         return self.title

    def pub_date_revised(self):
        return self.pub_date.strftime('%b %e %Y')
