
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('form/', views.uploadForm, name='form'),
    path('upload/', views.uploadFile, name='uload'),
    path('files/', views.FileView.as_view(), name='files'),
]