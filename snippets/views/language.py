from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from snippets.models.language import Language
from snippets.models.snippet import Snippet

class LanguageCreateView(CreateView):
    model = Language
    template_name = ""

class LanguageListView(ListView):
    model = Snippet
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Language Snippets"
        context['object_list'] = Snippet.objects.filter(language_id=self.kwargs['pk'])
        return context

class LanguageUpdateView(UpdateView):
    model = Language
    template_name = ""

class LanguageDeleteView(DeleteView):
    model = Language
    template_name = ""
