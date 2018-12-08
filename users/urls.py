# users.urls
from django.urls import include, path

from .views import UserRetrieveView, UserFindEmailView, UserFindUsernameView

urlpatterns = [
    path('', UserRetrieveView.as_view()),
    path('checkEmail', UserFindEmailView.as_view()),
    path('checkUsername', UserFindUsernameView.as_view()),
]
