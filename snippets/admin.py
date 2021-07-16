from django.contrib import admin

from snippets.models.language import Language
from snippets.models.snippet import Snippet

admin.site.register(Language)
admin.site.register(Snippet)
