from django.forms import ModelForm, Form

from snippets.models.snippet import Snippet

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = []