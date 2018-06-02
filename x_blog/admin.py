from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag


# 注册
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['title', 'created_time', 'category']
    #设置每页要显示在列表中多少条记录，默认是100我这里设置成50
    list_per_page = 50
    # 筛选器
    list_filter =('title', 'category') #过滤器
    search_fields =('title',) #搜索字段
    date_hierarchy = 'created_time'    # 详细时间分层筛选　



# admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
