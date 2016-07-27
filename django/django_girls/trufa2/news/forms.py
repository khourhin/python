from django import forms
from .models import NewsPost

class NewsForm(forms.ModelForm):

    class Meta:
        model = NewsPost
        fields = ('title', 'text',)
