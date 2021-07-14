from django.urls import path
from django.contrib.auth.views import LogoutView

from snippets.views.snippets import *
from snippets.views.user import *
from snippets.views.language import *

app_name = "snippets"

urlpatterns = [
    path('', SnippetListView.as_view(), name='index'),
    path('login/', LoginAppView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('snippets/python/', LanguageListView.as_view(), name='language'),
    path('snippets/user/juancito/', UserSnippetsView.as_view(), name='user_snippets'),
    path('snippets/snippet/', SnippetDetailView.as_view(), name='snippet'),
    path('snippets/add/', SnippetCreateView.as_view(), name='snippet_add'),
    path('snippets/edit/', SnippetUpdateView.as_view(), name='snippet_edit'),
    path('snippets/delete/', SnippetDeleteView.as_view(), name='snippet_delete'),
]