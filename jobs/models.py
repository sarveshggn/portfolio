from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='image/')
    summary = models.CharField(max_length=255)
    github_link = models.CharField(max_length=300, default='#')

    def __str__(self):
        return self.summary