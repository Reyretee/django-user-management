from atexit import register
from django.urls import path, include
from users.views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', register, name="register"),
    path('oauth/', include("social_django.urls")),
]
