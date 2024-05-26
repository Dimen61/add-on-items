from django.urls import path
from . import views

app_name = 'addon_items'
urlpatterns = [
    path("", views.index, name='index'),
    path('add', views.add, name='add'),
    path('target', views.target, name='target'),
    path("<str:name>", views.greet, name='greet')
]