from django.contrib import admin

from .models import Post, Comment # models.pyで指定したクラス名

admin.site.register(Post) # models.pyで指定したクラス名
admin.site.register(Comment) # models.pyで指定したクラス名
