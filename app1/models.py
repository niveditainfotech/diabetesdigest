from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
  title =  models.CharField(max_length=200, unique=True)
  slug =   models.SlugField(max_length=200, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
  created_on = models.DateTimeField()
  updated_on = models.DateTimeField(auto_now=True)
  content = models.TextField()
  status = models.IntegerField(choices=STATUS, default=0)
  

  class Meta:
    ordering = ['-created_on']

  def __str__(self):
    return self.title
  
class Reviews(models.Model):
  Name=models.CharField(max_length=50)
  Designation=models.CharField(max_length=100)
  Review=models.TextField()
  upload=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.Name
  
class Links(models.Model):
  Description=models.CharField(max_length=300)
  Link=models.CharField(max_length=1000)
  created=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.Description