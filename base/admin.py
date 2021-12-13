from django.contrib import admin
from .models import (
    Website,
    Product,
    User
)

def register(model):
    admin.site.register(model)

register(Website)
register(Product)
register(User)