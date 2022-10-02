from django.urls import path
from .views import (
    list_view,
    list_view2,  
)

app_name = 'main'
urlpatterns = [
    path('', list_view, name='home-list'),
    path('join-now', list_view2, name='ex1'),
]
