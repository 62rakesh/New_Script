from django.contrib import admin

# Register your models here.
from .models import Tag
from .models import customer
from .models import Products
from .models import Order
from .models import events
admin.site.register(customer)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(events)