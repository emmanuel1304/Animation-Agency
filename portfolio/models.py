from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.name        

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='project', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    video = CloudinaryField(resource_type='video')

    def __str__(self):
        return self.title        