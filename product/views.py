from django.shortcuts import render,get_object_or_404,redirect
from .models import Products,Category
from .forms import Addcategoryform,Addproduct
from django.contrib import messages
from django import views




def category_view(request):
    cat=Category.objects.filter(status=0)
    return render(request,"product_catgory.html",{"cat":cat})


def product_view(request):
    pro=Products.objects.filter(status=0)
    return render(request,"product_category.html",{"pro":pro})


def AddcategoryView(request):
    forms=Addcategoryform()
    if request.method=="POST":
        forms=Addcategoryform(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request,"Kategoriya muvaffaqiyatli qo'shildi")
            return redirect("page_category")
    context={
        "forms":forms
    }
    return render(request,"cat_add.html",context)





def Addprodukt(request):
    forms=Addproduct()
    if request.method=="POST":
        forms=Addproduct(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request,"Product muvaffaqiyatli qo'shildi")
            return redirect("saxifa")
    context={
        "forms":forms
    }
    return render(request,"add_pro.html",context)





















def CategoryDetailView(request,slug):
    if (Category.objects.filter(slug=slug,status=0)):
        products=Products.objects.filter(category__slug=slug)
        category_name=Category.objects.filter(slug=slug).first()
        context={
            'products':products,
            'category_name':category_name
        }
        return render(request,"category_allproducts.html",context)
    else:
        messages.warning(request,"Bu kategoriyada hozircha tovar yo'q")
        return redirect('cat')









