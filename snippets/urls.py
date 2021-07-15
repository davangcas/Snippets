from django.urls import path
from django.contrib.auth.views import LogoutView

from snippets.views.snippets import *
from snippets.views.user import *
from snippets.views.language import *

app_name = "snippets"

urlpatterns = [
    path('', SnippetListView.as_view(), name='index'),
    path('login/', LoginAppView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='snippets:login'), name='logout'),
    path('snippets/<int:pk>/', LanguageListView.as_view(), name='language'),
    path('snippets/user/<int:pk>/', UserSnippetsView.as_view(), name='user_snippets'),
    path('snippets/snippet/<int:pk>/', SnippetDetailView.as_view(), name='snippet'),
    path('snippets/add/<int:pk>/', SnippetCreateView.as_view(), name='snippet_add'),
    path('snippets/edit/<int:pk>/', SnippetUpdateView.as_view(), name='snippet_edit'),
    path('snippets/delete/<int:pk>/', SnippetDeleteView.as_view(), name='snippet_delete'),
]