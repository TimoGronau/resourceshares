from django.contrib import admin
from apps.resources.models import Resources, Review,Tag, Category, ResourcesTag,Rating

class CustomResources(admin.ModelAdmin):
    list_display = (
        "username",
        "user_title",
        "title",
        "link",
        "get_tags",
        "description",
    )
    
    def username(self, obj):
        return obj.user_id.username

    def user_title(self,obj):
        return obj.user_id.title
        
    @admin.display(description="Tags")
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    
    
class CustomRatings(admin.ModelAdmin):
    list_display=(
        "username",
        "resource",
        "get_rating",
    )
    
    @admin.display(description="Rating")
    def get_rating(self,obj):
        return obj.rate
    
    
class CustomReviews(admin.ModelAdmin):
    list_display = (
        "username",
        "resource",
        "get_review",
    )
    
    @admin.display(description="Review")
    def get_review(self,obj):
        return obj.get_body
    

class CustomResourcesTag(admin.ModelAdmin):
    list_display = (
        "title",
        "tag",
    )
    
    

admin.site.register(Resources, CustomResources)
admin.site.register(Review, CustomReviews)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Rating, CustomRatings)
admin.site.register(ResourcesTag, CustomResourcesTag)
# Register your models here.
