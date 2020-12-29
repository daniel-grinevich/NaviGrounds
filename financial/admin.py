from django.contrib import admin
from .models import Payment, Category, Status

#Register your models here.
admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(Status)
