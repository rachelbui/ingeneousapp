from django.db import models
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    genre = models.CharField(max_length=128)
    chapter = models.CharField(max_length=64)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=False, null=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def update(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
