from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,db_index=True)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name
