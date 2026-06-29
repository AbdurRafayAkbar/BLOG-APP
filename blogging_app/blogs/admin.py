from django.contrib import admin
from .models import Blogs


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ["author", "blog_title", "slug", "publish", "Status"]
    list_filter = ["Status", "created_at", "publish", "author"]
    search_fields = ["author__username", "blog_title"]
    prepopulated_fields = {"slug": ("blog_title",)}
    show_facets = admin.ShowFacets.ALWAYS