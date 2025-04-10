from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shop, name = "shop"),
    path('create', views.new, name ='new'),
    path('new', views.create, name='create'),
    path('<str:id>', views.detail, name ='detail'),
    path('<str:id>/edit', views.edit, name='edit'),
    path('<str:id>/update', views.update, name='update'),
    path('<str:id>/delete', views.delete, name='delete'),
]