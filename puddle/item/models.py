from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Batch Name'

    def __str__(self):
        return self.name

class Item(models.Model):
    batch_name = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_join = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Student Name'

    def __str__(self):
        return self.name
