from django.urls import path
from . import views

app_name = 'portfolio'


urlpatterns = [ 
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio_detail/<int:id>/', views.portfolio_detail, name='portfolio_detail'),
    path('sub_category_detail/<int:id>/', views.sub_category_detail, name='sub_category_detail'),
]