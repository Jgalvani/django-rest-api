from django.urls import path

from . import views


app_name = 'products'

urlpatterns = [ 
    path('', views.productList.as_view(), name='products'),
    path('<int:id>', views.productDetail.as_view(), name='product'),
    path('categories', views.categoryList.as_view(), name='categories'),
    path('categories/<int:id>', views.categoryDetail.as_view(), name='category'),
    path('customers', views.customerList.as_view(), name='customers'),
    path('customers/<int:id>', views.customerDetail.as_view(), name='customer'),
    path('orders', views.orderList.as_view(), name='orders'),
    path('orders/<int:id>', views.orderDetail.as_view(), name='order'),
]
