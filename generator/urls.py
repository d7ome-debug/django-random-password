# App urls
from django.urls import path
from .views import * #import everythin in your views.py


urlpatterns = [
    path('', home, name='home'), # this is my main page (views.home is gonna be my view name)(name='home' we use this to locate the url in the templates or html)
    path('password/', password, name="password"),
]