from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'role')
    search_fields = ('email', 'username')
    readonly_fields = ('username', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(ShopName)
admin.site.register(Coffee)
admin.site.register(RecommendedCoffee)
admin.site.register(IsFavourite)
admin.site.register(Order)
