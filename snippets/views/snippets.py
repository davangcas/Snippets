from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from snippets.models.snippet import Snippet

class SnippetCreateView(CreateView):
    model = Snippet
    template_name = "snippets/snippet_add.html"