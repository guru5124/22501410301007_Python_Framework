from django.contrib import admin
from .models import ContactUs, Registration, Post, Category

admin.site.register(ContactUs)
admin.site.register(Registration)
admin.site.register(Post)
admin.site.register(Category)