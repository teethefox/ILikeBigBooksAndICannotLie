from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book, User
admin.site.register(Book)
admin.site.register(User)
# admin.site.register(Book)
# admin.site.register(Author)