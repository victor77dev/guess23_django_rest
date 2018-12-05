# games.urls
from django.urls import include, path

from .views import GameListCreateView

urlpatterns = [
    path('', GameListCreateView.as_view()),
]
