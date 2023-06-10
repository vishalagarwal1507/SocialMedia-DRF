from django.contrib import admin

# Register your models here.
from .models import Folder, File

admin.site.register(File)
# admin.site.register(Folder)