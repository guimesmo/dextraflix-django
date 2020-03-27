import datetime

from django.db import models
from django.utils.text import slugify

from video.utils import extract_video_id


class Author(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.TextField()
    email = models.EmailField(max_length=255)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.TextField()

    class Meta:
        ordering = ("name", "id", )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Video(models.Model):
    name = models.CharField(max_length=255)
    video_date = models.DateField(default=datetime.date.today)
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    hashtags = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

    @property
    def video_id(self):
        return extract_video_id(self.url)

    def thumbnail(self):
        return f"https://img.youtube.com/vi/{self.video_id}/0.jpg"
