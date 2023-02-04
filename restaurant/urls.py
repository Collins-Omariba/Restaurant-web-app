from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menuitem/<int:pk>/', views.display_menu_item, name="menu_item"),


    path('menu-api', views.MenuItemView.as_view()),
    path('menuitem-api/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking-api', include(router.urls)),
    path('api-token-auth', obtain_auth_token)
                                                    
]

