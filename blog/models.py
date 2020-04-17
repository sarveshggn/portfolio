from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title

    def pub_date_simple(self):
        return self.pub_date.strftime('%d %b %Y')

    def summary(self):
        return self.body[:100]