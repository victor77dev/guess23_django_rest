# gamerooms.urls
from django.urls import include, path

from .views import GameroomCreateView, GameroomListView

urlpatterns = [
    path('', GameroomListView.as_view()),
    path('create', GameroomCreateView.as_view()),
]
