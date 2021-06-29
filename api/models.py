from django.db import models

from pathlib import Path
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


class SingletonModel(models.Model):
    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        
        pass
        
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class BasePath(SingletonModel):
    path = models.CharField(max_length=10000, default="", blank=True, null=True)

class ScreenshotParse(models.Model):
    path = models.CharField(max_length=10000, unique=True, blank=False, null=False)
    text = models.TextField(default="")