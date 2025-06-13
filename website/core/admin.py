from django.contrib import admin
from .models import Country, Category, User

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Category)
