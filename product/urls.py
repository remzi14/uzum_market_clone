from .views import category_view,AddcategoryView,CategoryDetailView,product_view,Addprodukt
from django.urls import path

urlpatterns=[
    path("category/",category_view,name="page_category"),
    path("add_cat/",AddcategoryView,name="addcat"),
    path("add_pro/",Addprodukt,name="addpro"),
    path("product/",product_view,name="pro"),
    path("category/detail/<str:slug>/",CategoryDetailView,name="detcat"),
]
