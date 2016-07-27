from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    # Modify the look of the admin part to deal with the "post" model
    list_display = ('title', 'timestamp', 'updated')
    list_display_links = ['updated']
    # Make fields directly editable
    list_editable = ['title']
    # Add the "filter" pane in /admin/post/post
    list_filter = ['timestamp', 'updated']
    # Add a search field in /admin/post/post
    search_fields = ['title', 'content']
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
