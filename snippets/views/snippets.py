from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render

from pygments import highlight
import pygments.lexers as lx
from pygments.formatters import HtmlFormatter

from snippets.models.snippet import Snippet
from snippets.forms.snippets import SnippetForm


class SnippetCreateView(CreateView):
    model = Snippet
    form_class = SnippetForm
    template_name = "snippets/snippet_add.html"
    success_url = reverse_lazy('snippets:index')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = self.request.user
            snippet.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.object = None
            context = self.get_context_data(**kwargs)
            return render(request, self.template_name, context)

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
    template_name = "snippets\snippet_edit.html"
    form_class = SnippetForm
    success_url = reverse_lazy('snippets:index')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edit Snippet"
        return context

class SnippetDeleteView(DeleteView):
    model = Snippet
    template_name = "snippets/snippet_delete.html"
    success_url = reverse_lazy('snippets:index')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Delete Snippet"
        return context

class SnippetDetailView(TemplateView):
    template_name = "snippets/snippet.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Snippet Detail"
        context['snippet'] = Snippet.objects.get(pk=self.kwargs['pk'])
        snip_lang = Snippet.objects.get(pk=self.kwargs['pk']).language.slug
        lexer = lx.get_lexer_by_name(snip_lang)
        context['code'] = highlight(Snippet.objects.get(pk=self.kwargs['pk']).snippet, lexer, HtmlFormatter(), outfile=None)
        return context