from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class sum_form(forms.Form):
     edit1 = forms.CharField()
     edit2 = forms.CharField()
     #edit_result = forms.CharField(disabled = True)
     edit_result = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
     #edit_result = forms.CharField()

