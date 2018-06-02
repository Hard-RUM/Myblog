from django.contrib import admin
from .models import Comment

# Register your models here.
# 为了让 admin 界面管理某个数据模型，我们需要先注册该数据模型到 admin。比如，我们之前在 Model 中已经创建了模型 Comment
admin.site.register(Comment)