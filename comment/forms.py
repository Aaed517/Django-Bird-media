from django import forms
from crispy_forms.helper import FormHelper

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea, label='Yorum Yap', max_length=600)

class CommentPopupForm(forms.Form):
    commentpopup = forms.CharField(widget=forms.Textarea, label='Yorum Yap', max_length=600)

class SubCommentForm(forms.Form):
    subcomment = forms.CharField(widget=forms.Textarea, label='Yorum Yap', max_length=600)