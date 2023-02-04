from django.contrib import admin
from .models import Menu, Booking, BookingTemplate, MenuTemplate
# Register your models here.

admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(MenuTemplate)
admin.site.register(BookingTemplate)