# server/djangoapp/urls.py

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for login
    path('login', views.login_user, name='login'),
    # path for logout
    path('logout', views.logout_user, name='logout'),
    path('register', views.logout_user, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
