from warriors import views
from django.urls import path
from warriors.views import Warriors


urlpatterns = [
    path('', views.index, name='home'),
    path('warriors/', Warriors.as_view(), name='warriors'),
]
