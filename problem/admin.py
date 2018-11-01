from django.contrib import admin
from .models import Problems
from .models import Tag

@admin.register(Problems)
class Problems_admin(admin.ModelAdmin):
    list_display = ("id", "Headline","Author","last_updated_time")
    ordering = ("-last_updated_time",)  


@admin.register(Tag)
class Tag_admin(admin.ModelAdmin):
    list_display = ("Tag_name",)
