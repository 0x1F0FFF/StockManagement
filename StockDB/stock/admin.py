from django.contrib import admin
from .models import InventoryItem, Location, Category

admin.site.register(InventoryItem)
admin.site.register(Location)
admin.site.register(Category)

