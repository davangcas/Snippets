from django.views.generic import TemplateView

class LoginAppView(TemplateView):
    template_name = "snippets/login.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UserSnippetsView(TemplateView):
    template_name = "snippets/user_snippets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
