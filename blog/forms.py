from django import forms

from .models import Post, PythonExample, VisitorsInfo

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'subtitle', 'difficulty', 'learned', 'text')


class PythonExampleForm(forms.ModelForm):
    class Meta:
        model = PythonExample
        fields = ('author', 'title', 'text')

class VisitorsInfoForm(forms.ModelForm):
    class Meta:
        model = VisitorsInfo
        fields = ('name', 'knowDjango', 'skillsDjango')
