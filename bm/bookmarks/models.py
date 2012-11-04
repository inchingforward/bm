from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    notes = models.TextField(null=True, blank=True)
    private = models.BooleanField()
    tags = TaggableManager()
    user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-create_date']
    
    def __unicode__(self):
        return self.title

