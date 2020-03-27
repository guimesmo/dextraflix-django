from django.contrib import admin
from .models import Video, Author, Category

admin.site.register([Video, Author, Category])
