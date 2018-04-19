from django.contrib import admin

# Register your models here.
from .models import Image
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created','tag_list']
    list_filter = ['created']
    def get_queryset(self, request):
        return super(ImageAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
    

admin.site.register(Image, ImageAdmin)

    