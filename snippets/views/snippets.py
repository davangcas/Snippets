from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from snippets.models.snippet import Snippet

class SnippetCreateView(CreateView):
    model = Snippet
    template_name = "snippets/snippet_add.html"

class SnippetListView(ListView):
    model = Snippet
    template_name = "snippets/snippets.html"

class SnippetUpdateView(UpdateView):
    model = Snippet
    template_name = "snippets/snippets_update.html"

class SnippetDeleteView(DeleteView):
    model = Snippet
    template_name = "snippets/snippets_delete.html"