from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)

def __str__(self):
    return self.title

class Comment(models.Model):
    user_id = models.IntegerField()
    comment = models.TextField()
    article_id = models.IntegerField()