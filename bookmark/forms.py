from django import forms
from .models import Bookmark

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['movie_name', 'review_text', 'view_count']
