"""
URL configuration for LittleLemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from restaurant import views

booking_router = DefaultRouter()
booking_router.register(r'tables', views.BookingViewSet, basename='booking')

api_booking_router = DefaultRouter()
api_booking_router.register(r'', views.BookingViewSet, basename='api-booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(booking_router.urls)),
    path('api/bookings/', include(api_booking_router.urls)),
    path('api/menu-items/', views.MenuItemsView.as_view(), name='api-menu-items'),
    path(
        'api/menu-items/<int:pk>/',
        views.SingleMenuItemView.as_view(),
        name='api-menu-item-detail',
    ),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
