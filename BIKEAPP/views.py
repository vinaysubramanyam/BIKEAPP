from django.shortcuts import render
from django.views.generic import FormView, DetailView, ListView
from bike.models import Category

def about(request):
	return render(request,"about.html", {})

def private(request):
	return render(request,"private.html", {})


def newsform(request):
    category_list=Category.objects.order_by('-likes')[:]
    context_dict={'categories':category_list}
    return render(request,"news.html", context_dict)


