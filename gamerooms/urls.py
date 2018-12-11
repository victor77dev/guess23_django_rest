# gamerooms.urls
from django.urls import include, path

from .views import GameroomCreateView, GameroomListView, GameroomListDetailView

urlpatterns = [
    path('', GameroomListView.as_view()),
    path('create', GameroomCreateView.as_view()),
    path('detail', GameroomListDetailView.as_view()),
]
