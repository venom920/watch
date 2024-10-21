from django.contrib import admin
from admin_app.models import *
from watch_app .admin import *

# Register your models here.
admin.site.register(Register)
admin.site.register(Login)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Checkout)
admin.site.register(Contact)
