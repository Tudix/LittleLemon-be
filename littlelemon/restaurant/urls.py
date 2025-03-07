from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuItemView.as_view(), name='menu-item'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
]