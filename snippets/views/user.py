from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from snippets.models.snippet import Snippet

class LoginAppView(LoginView):
    template_name = "login.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('snippets:index')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UserSnippetsView(TemplateView):
    template_name = "snippets/user_snippets.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.object.get(pk=self.kwargs['pk'])
        context['public_snippets'] = Snippet.objects.filter(user_id=self.kwargs['pk']).filter(public=True)
        if self.request.user.id == User.objects.get(pk=self.kwargs['pk']):
            context['private_snippets'] = Snippet.objects.filter(user_id=self.kwargs['pk']).filter(public=False)
        return context
