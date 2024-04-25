from django.urls import path
from .views import Categories_View,AddcetegoryView,AddpoductView,Product_View
urlpatterns = [
    path('category/',Categories_View,name="cate"),
    path('produc/',Product_View,name="pro_v"),
    path('addcategory/',AddcetegoryView,name="add_cat"),
    path('adproduct/',AddpoductView,name="add_pro"),
]


