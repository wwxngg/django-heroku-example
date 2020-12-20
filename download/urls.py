from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('title/<path:url>', views.title, name='title'),
    path('download/<path:url>', views.download, name='download'),
]
