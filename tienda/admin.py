from django.contrib import admin

from django.contrib import admin
from .models import Categoria, Producto, Contact
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)


class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'contact_type', 'created_at', 'subscription')
    search_fields=('name', 'email', 'message')
    list_filter =('name', 'email')


admin.site.register(Contact, ContactAdmin)