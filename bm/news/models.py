from django.db import models
from django.contrib.auth.models import User


class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-create_date']
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('news_item', kwargs={'pk': self.pk})
