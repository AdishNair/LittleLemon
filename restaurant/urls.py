from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


app_name = 'restaurant'

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/items/', views.MenuItemsView.as_view(), name='menu-items-alias'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item'),
    path(
        'menu/items/<int:pk>/',
        views.SingleMenuItemView.as_view(),
        name='menu-item-alias',
    ),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
