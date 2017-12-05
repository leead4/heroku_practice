from django.contrib import admin
admin.site.register (Tags)
admin.site.register (Animation)
admin.site.register (Asset)
admin.site.register (Content)
admin.site.register (Author)
admin.site.register (Post)

# class TagsAdmin(admin.ModelAdmin):
# 	fields = ('topic')

# class AnimationAdmin(admin.ModelAdmin):
# 	fields = ('style')

# class AssetAdmin(admin.ModelAdmin):
# 	fields = ('file_path','animation','image_data')

# class ContentAdmin(admin.ModelAdmin):
# 	fields = ('text', 'asset')

# class AuthorAdmin(admin.ModelAdmin):
# 	fields = ('name', 'avatar')

# class PostAdmin(admin.ModelAdmin):
# 	fields = ('content', 'title', 'post_like', 'post_type', 'date', 'tags', 'author')
