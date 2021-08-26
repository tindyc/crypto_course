from django.contrib import admin
from .models import BlogPost, BlogComment

# Register your models here.


class BlogCommentInline(admin.TabularInline):
    """ Allows view/edit of blog comments from Blog detail page """

    model = BlogComment


class BlogAdmin(admin.ModelAdmin):
    """ Creates the admin interface for Blog posts """

    list_display = (
        'blog_title',
        'author',
        'blog_content',
        'date'
    )

    inlines = [
        BlogCommentInline,
    ]


class BlogCommentAdmin(admin.ModelAdmin):
    """ Creates the admin interface for Blog Comment """
    
    list_display = (
        'comment_title',
        'comment',
        'blogpost',
        'comment_user'
    )


admin.site.register(BlogPost, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)