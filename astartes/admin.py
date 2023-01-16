from django.contrib import admin
from .models import Marine,Post,CustomUser

# Register your models here.

admin.site.register(Marine)
admin.site.register(Post)
admin.site.register(CustomUser)