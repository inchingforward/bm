from django.forms import ModelForm
from bm.bookmarks.models import Bookmark


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        exclude = ('user',)