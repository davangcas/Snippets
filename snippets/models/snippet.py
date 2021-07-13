from django.db import models
from django.contrib.auth.models import User

from snippets.models.language import Language

class Snippet(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    language = models. ForeignKey(Language, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    snippet = models.TextField()
    public = models.BooleanField(default=False)