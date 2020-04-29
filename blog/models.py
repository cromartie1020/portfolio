from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=60)
    body=models.TextField()
    pub_date=models.DateTimeField()
    image=models.ImageField(upload_to='images/', default='default.jpg')


    def __str__(self):
        return self.title
