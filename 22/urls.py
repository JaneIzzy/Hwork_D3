from django.urls import path

from .views import ProductList, ProductDetail

urlpatterns = [

    path('',

    path('<int:pk>', ProductDetail.as_view())
]