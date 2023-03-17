from django.shortcuts import render
from .models import Project, Category
# Create your views here.


def home(request):
    return render(request, 'portfolio/home.html')

def portfolio(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
        
    if category_id:
        projects = Project.objects.filter(category=category_id)
    else:
        projects = Project.objects.filter(category=1)
    context = {'categories':categories, 'projects':projects}    
    return render(request, 'portfolio/portfolio.html', context)
