from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user')
    
    
class PlanAttributeInline(admin.TabularInline):
    model = PlanAttribute
    
    
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'customer')
    inlines = (PlanAttributeInline,)
