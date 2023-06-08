from django.contrib import admin
from .models import Gametest

# Register your models here.
@admin.register(Gametest)
class myadmin(admin.ModelAdmin) :
    actions = ['delete_selected']
    list_display = ('name', 'description', 'price' , 'created_at' , 'updated_at')
    list_editable = ('price',)
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'description')

    def delete_selected(self , request , queryset) :
        queryset.delete()
        pass
    pass