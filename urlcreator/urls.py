
from django.urls import path
from .views import shortened_url

urlpatterns = [
    path('<str:token>', shortened_url, name="shortened_url")

]
