from django.db import models

class CreatedModifiedDateTimeBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) # auto create datetime and set editable = False
    
    class Meta:
        abstract = True