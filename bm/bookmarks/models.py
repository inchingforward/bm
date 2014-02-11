from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.TextField()
    description = models.TextField()
    
    def __unicode__(self):
        return self.name

class Bookmark(models.Model):
    url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200)
    notes = models.TextField(null=True, blank=True)
    private = models.BooleanField()
    tags = TaggableManager(blank=True)
    user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True)
    
    class Meta:
        ordering = ['-create_date']
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('bookmark_detail', kwargs={'pk': self.pk})

