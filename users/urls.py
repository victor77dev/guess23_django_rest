# users.urls
from django.urls import include, path

from .views import UserRetrieveView, UserFindEmailView

urlpatterns = [
    path('', UserRetrieveView.as_view()),
    path('checkEmail', UserFindEmailView.as_view()),
]
