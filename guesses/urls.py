# guesses.urls
from django.urls import include, path

from .views import GuessCreateView, GuessListView, GuessListAllView

urlpatterns = [
    path('', GuessListView.as_view()),
    path('create', GuessCreateView.as_view()),
    path('all', GuessListAllView.as_view()),
]
