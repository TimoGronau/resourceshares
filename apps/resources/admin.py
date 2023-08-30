from django.contrib import admin
from apps.resources.models import Resources, Review,Tag, Category, ResourcesTag,Rating

class CustomResources(admin.ModelAdmin):
    list_display = (
        "username",
        "user_title",
        "title",
        "link",
        "description"
    )

admin.site.register(Resources, CustomResources)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Rating)
# Register your models here.
