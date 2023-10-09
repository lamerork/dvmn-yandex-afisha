from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html

# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image
    fields = ['image', 'preview_image', 'position']
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        width = obj.image.width * 200/obj.image.height
        return format_html('<img src="{}" width="{}px" height="200px" />', obj.image.url, width)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass