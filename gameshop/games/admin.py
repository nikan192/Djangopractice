from django.contrib import admin
from .models import Games , Special_Games

# Register your models here.


@admin.register(Games , Special_Games)
class Myadmin(admin.ModelAdmin) :
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
