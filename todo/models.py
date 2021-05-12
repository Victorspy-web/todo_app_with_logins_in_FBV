from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    complete = models.BooleanField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']