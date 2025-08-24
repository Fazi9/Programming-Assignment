from django.urls import path
from . import views

urlpatterns = [
    # Staff portal URLs
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Customer portal URLs
    path('menu/', views.customer_menu_view, name='customer_menu'),
    path('add_to_cart/<int:pk>/', views.add_to_cart_view, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order_placed/', views.order_placed_view, name='order_placed'),

    # Orders
    path('orders/', views.order_list_view, name='order_list'),

    # This is the corrected path for the staff menu list
    # It now has a unique URL to avoid conflict.
    path('menu/list/', views.menu_list_view, name='menu_list'),
]