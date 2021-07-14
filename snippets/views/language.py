from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from snippets.models.language import Language

class LanguageCreateView(CreateView):
    model = Language
    template_name = ""

class LanguageListView(ListView):
    model = Language
    template_name = ""

class LanguageUpdateView(UpdateView):
    model = Language
    template_name = ""

class LanguageDeleteView(DeleteView):
    model = Language
    template_name = ""
