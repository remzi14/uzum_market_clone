from .models import Category,Products
from django.forms import ModelForm


class Addcategoryform(ModelForm):
    class Meta:
        model=Category
        fields="__all__"




class Addproduct(ModelForm):
    class Meta:
        model=Products
        fields="__all__"






