from .models import Offer
from django import forms
from django.contrib import admin

class Admin_Price(admin.ModelAdmin):
    list_display = ("name", "price", "description")
    list_display_links = ("name",)
admin.site.register(Offer, Admin_Price)