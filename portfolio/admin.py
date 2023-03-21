from django.contrib import admin
from .models import Project, Category, SubCategory
# Register your models here.


admin.site.register(Category)
admin.site.register(Project)
admin.site.register(SubCategory)