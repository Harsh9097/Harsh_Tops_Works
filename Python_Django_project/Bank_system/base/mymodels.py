from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    deleted_at = models.DateTimeField(null=True , blank=True , default=None)
    
    def delete(self,*args, **kwargs):
        self.deleted_at=timezone.now()
        self.save()
        
    deleted = models.BooleanField(default=False)
    
    def delete(self,*args, **kwargs):
        self.deleted_at=timezone.now()
        self.deleted=True
        self.save()
    class Meta:
        abstract = True


    deleted = models.BooleanField(default=False)
    
    def delete(self,*args, **kwargs):
        self.deleted_at=timezone.now()
        self.deleted=True
        self.save()