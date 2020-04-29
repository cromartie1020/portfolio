from django.db import models


class Mymail(models.Model):

    subject=models.CharField(max_length=255)
    message=models.TextField()
    From=models.EmailField('cromarties2913@gmail.com')
    To=models.EmailField(blank=False)

    def __str__(self):
        return self.subject
