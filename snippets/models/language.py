from django.db import models

class Language(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    slug = models.CharField(verbose_name="Slug", max_length=50)