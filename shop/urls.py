from django.urls import path

from shop import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product/buy/', views.product_buy, name='product_buy'),
    path('basket/', views.basket, name='basket'),
    path('purchase/', views.purchase, name='purchase'),
    path('payment/', views.payment, name='payment'),
]
