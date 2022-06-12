from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User 


# Create your models here. 
class Category(models.Model):
    title = models.CharField(max_length=100) 

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catg-detail', args=[self.pk]) 


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catgs')
    image = models.FileField(upload_to='posts/%Y/%B %d', blank=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date',] 
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f"{self.category} - {self.title} - {self.date}" 
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk])



