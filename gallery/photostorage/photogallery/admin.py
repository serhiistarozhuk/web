from django.contrib import admin
from .models import picture, comment


class PictureInline(admin.StackedInline):
    model = comment
    extra = 2


class PictureAdmin(admin.ModelAdmin):
    fields = ['pic_title', 'pic_text', 'pic_thumb', 'pic_image', 'pic_date']          # this class allows custom output fields, visible in admin panel
    readonly_fields = ['pic_thumb']
    list_filter = ['pic_date']    # sort filter
    list_display = ['pic_title', 'pic_text', 'pic_thumb']    # fields for output in general admin view
    inlines = [PictureInline]
  
admin.site.register(picture, PictureAdmin)
