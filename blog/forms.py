from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class sum_form(forms.Form):
     edit1 = forms.CharField()
     edit2 = forms.CharField()
     edit_result = forms.CharField()

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
