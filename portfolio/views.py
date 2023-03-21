from django.shortcuts import render, get_object_or_404
from .models import Project, Category, SubCategory
# Create your views here.


def home(request):
    return render(request, 'portfolio/home.html')

def portfolio(request):
    category = Category.objects.all()
    context = {'category':category}
    return render(request, 'portfolio/portfolio.html', context)

def portfolio_detail(request, id):
    category = Category.objects.get(id=id)
    context = {'category':category}
    return render(request, 'portfolio/portfolio_detail.html', context)    