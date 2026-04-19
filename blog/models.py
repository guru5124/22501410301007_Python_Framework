from django.db import models

# CONTACT US MODEL
class ContactUs(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    comment = models.TextField()
    def __str__(self):
        return self.name if self.name else "No Name"
# POST MODEL
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    def __str__(self):
        return self.title
# CATEGORY MODEL
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
    
# Registation
class Registration(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name