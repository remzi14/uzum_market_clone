from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Products
from .forms import Addcategory,Addproduct
from django.contrib import messages
# Create your views here.

def Categories_View(request):
    category = Category.objects.filter(status=0)
    return render(request,'categor.html',{"category":category})


def Product_View(request):
    pro = Products.objects.filter(status=0)
    return render(request,"product.html",{"pro":pro})




def AddcetegoryView(request):
    forms=Addcategory()
    if request.method=="POST":
        forms=Addcategory(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request,"Kategoriya yaxshi qo'shildi")
            return redirect("cate")
    context={
        "forms":forms

    }
    return render(request,"add_cat.html",context)







def AddpoductView(request):
    forms=Addproduct()
    if request.method=="POST":
        forms=Addproduct(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request,"Yangi product yaxshi qo'shildi !")
            return redirect("pro_v")
    context={
        "forms":forms
    }
    return render(request,"add_product.html",context)









