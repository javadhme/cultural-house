from warriors import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('warriors/', views.warriors, name='warriors'),
]
