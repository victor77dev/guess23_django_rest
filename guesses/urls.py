# guesses.urls
from django.urls import include, path

from .views import GuessCreateView, GuessListView, GuessUpdateView, GuessListAllView

urlpatterns = [
    path('', GuessListView.as_view()),
    path('create', GuessCreateView.as_view()),
    path('update', GuessUpdateView.as_view()),
    path('all', GuessListAllView.as_view()),
]
