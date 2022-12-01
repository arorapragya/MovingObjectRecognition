from django.contrib import admin
from .models import Video
# Register your models here.

@admin.register(Video)

class ImageAdmin(admin.ModelAdmin):
    list_display=['id','videofile']
