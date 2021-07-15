from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from snippets.models.snippet import Snippet
from snippets.forms.snippets import SnippetForm


class SnippetCreateView(CreateView):
    model = Snippet
    form_class = SnippetForm
    template_name = "snippets/snippet_add.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add Snippet"
        return context

class SnippetListView(ListView):
    model = Snippet
    template_name = "index.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Snippets"
        context['object_list'] = Snippet.objects.filter(public=True)
        return context

class SnippetUpdateView(UpdateView):
    model = Snippet
    template_name = "snippets/snippets_edit.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edit Snippet"
        return context

class SnippetDeleteView(DeleteView):
    model = Snippet
    template_name = "snippets/snippets_delete.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Delete Snippet"
        return context

class SnippetDetailView(TemplateView):
    template_name = "snippets/snippets.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Snippet Detail"
        context['snippet'] = Snippet.objets.get(pk=self.kwargs['pk'])
        return context