from django.contrib import admin
from .models import newsType
from .models import new
from .models import motto

@admin.register(newsType)
class newsType_admin(admin.ModelAdmin):
    list_display = ("id", "type_name")
    ordering = ("id",)  # 默认是倒叙 ordering = ("-id",)


@admin.register(new)
class new_admin(admin.ModelAdmin):
    list_display = ("id", "title", "newstype", "author", "is_deleted", "created_time", "last_updated_time")
    ordering = ("id",)  # 默认是倒叙 ordering = ("-id",)


@admin.register(motto)
class motto_admin(admin.ModelAdmin):
    list_display = ("id","mottoauthor","content")
    ordering = ("id",)


# Register your models here.
# admin.site.register(new,new_admin)
# admin.site.register(motto,motto_admin)


