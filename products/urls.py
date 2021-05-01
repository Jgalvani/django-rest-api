from django.urls import path

from . import views


app_name = 'products'

urlpatterns = [ 
    path('', views.productList.as_view(), name='products'),
    path('<int:pk>', views.productDetail.as_view(), name='product'),
]