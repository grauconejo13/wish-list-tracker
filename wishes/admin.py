from django.contrib import admin
from .models import WishItem, WishList

admin.site.register(WishList)
admin.site.register(WishItem)
