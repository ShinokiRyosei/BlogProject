from django import forms
from dblog.models import Article, User


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'article']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

