from django.contrib import admin

from .models import Menu, MenuItems



# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass



@admin.register(MenuItems)
class MenuItemsAdmin(admin.ModelAdmin):
    pass