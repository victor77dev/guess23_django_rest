# api.urls
from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls')),
    path('games/', include('games.urls')),
    path('gamerooms/', include('gamerooms.urls')),
    path('guesses/', include('guesses.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
