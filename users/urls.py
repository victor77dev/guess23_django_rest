# users.urls
from django.urls import include, path

from .views import UserRetrieveView

urlpatterns = [
    path('', UserRetrieveView.as_view()),
]
