from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'review']

class AnswerForm(forms.Form):
    fields = ['moviePk', 'answer']