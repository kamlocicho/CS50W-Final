from django.urls import path

from . import views

urlpatterns = [
    # Authentication routes
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('auth/create/', views.register, name='register'),

    path('', views.index, name='index'),
    path('product/<str:id>', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('cart/<str:product_id>', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<str:id>', views.remove_from_cart, name='remove_from_cart'),
    path('watchlist/<str:id>', views.watchlist, name='watchlist'),
]