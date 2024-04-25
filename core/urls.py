from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('favicon.ico', views.FaviconView.as_view(), name='favicon'),
]
