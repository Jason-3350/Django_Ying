from django.urls import path

from shop import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail')
]