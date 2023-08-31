from django.db import models
from django.contrib.postgres.fields import ArrayField
from apps.resources import validators
from apps.core.models import CreatedModifiedDateTimeBase


class Tag(CreatedModifiedDateTimeBase):
    #id =None if you dont want a default id to be created
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Category(CreatedModifiedDateTimeBase):
    cat= models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.cat
    
class Resources(CreatedModifiedDateTimeBase):
    user_id=models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    cat_id=models.ForeignKey("resources.Category", default=1, on_delete=models.SET_DEFAULT)
    title=models.CharField(max_length=200)
    description=models.TextField()
    link= models.URLField(max_length=500)
    tags = models.ManyToManyField("resources.Tag", through="ResourcesTag")
    #rate = ArrayField(base_field=models.IntegerField()) #INT ARRAY

    class Meta:
        verbose_name_plural = "Resources"

    def __str__(self):
        return f"{self.user_id.username} - {self.title}"

    @property
    def username(self):
        return self.user_id.username
    
    def user_title(self):
        return self.user_id.title
    
    def all_tags(self):
        return ", ".join([tag.name for tag in self.tags.all()])
    
class ResourcesTag(CreatedModifiedDateTimeBase):
    modified_at = None
    resources_id=models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    tag_id=models.ForeignKey("resources.Tag", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                "resources_id",
                "tag_id",
                name="resource_tag_unique",
                violation_error_message=f"Tag already exists for resource",
            )
        ]
        
    @property
    def title(self):
        return self.resources_id.title
    
    #making it a property or changing the display in admin has the same result (in the admin table) but different side effects
    @property
    def tag(self):
        return self.tag_id.name
        
    def __str__(self):
        return f"{self.resources_id.title}: {self.tag_id.name}"
    
class Review(CreatedModifiedDateTimeBase):
    user_id=models.ForeignKey("user.User", null=True , on_delete=models.SET_NULL)
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    body=models.TextField()
    
    @property
    def username(self):
        return self.user_id.username
    
    @property
    def resource(self):
        return self.resources_id.title
    
    @property
    def get_body(self):
        return self.body[:50]+"..."
    
    def __str__(self):
        return f"{self.user_id.username} - {self.resources_id.title}"
    
class Rating(CreatedModifiedDateTimeBase):
    user_id=models.ForeignKey("user.User", null=True , on_delete=models.SET_NULL)
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    rate=models.IntegerField(validators=[validators.check_rating_range])
    
    @property
    def username(self):
        return self.user_id.username
    
    @property
    def resource(self):
        return self.resources_id.title