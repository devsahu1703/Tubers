from django.contrib import admin
from .models import Youtuber
# Register your models here.
class YTAdmin(admin.ModelAdmin):
    list_display=('id','name','subs_count','is_featured')
    search_fields=('name','camera')
    list_filter=('name','camera')
    list_display_links=('name','id')
    list_editable=('is_featured',)

admin.site.register(Youtuber,YTAdmin)
