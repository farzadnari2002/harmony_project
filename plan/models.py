from django.db import models
from accounts.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer', verbose_name='کاربر')
    company_name = models.CharField(max_length=50, verbose_name='نام شرکت')
    
    
    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتری ها'
        
    def __str__(self):
        return self.company_name    
        

class Plan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='plans', verbose_name='مشتری')
    name = models.CharField(max_length=50, verbose_name='نام')
    price = models.IntegerField(verbose_name='قیمت')
    
    
    class Meta:
        verbose_name = 'برنامه'
        verbose_name_plural = 'برنامه ها'


class PlanAttribute(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='plan_attributes', verbose_name='برنامه')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.TextField(verbose_name='شرح')
    
    
    class Meta:
        verbose_name = 'ویژگی برنامه'
        verbose_name_plural = 'ویژگی های برنامه'

    
   
    
