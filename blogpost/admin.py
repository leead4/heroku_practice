from django.contrib import admin
from blogpost.models.models import *


admin.site.register (Tags)
admin.site.register (Asset)
admin.site.register (Content)
admin.site.register (Author)
admin.site.register (Post)

class TagsAdmin(admin.ModelAdmin):
 	fields = ('topic')

class AssetAdmin(admin.ModelAdmin):
	fields = ('image')

class ContentAdmin(admin.ModelAdmin):
	fields = ('text')

class AuthorAdmin(admin.ModelAdmin):
	fields = ('name', 'avatar')

class PostAdmin(admin.ModelAdmin):
	fields = ('content','asset', 'title', 'post_like', 'date', 'tags', 'author')
