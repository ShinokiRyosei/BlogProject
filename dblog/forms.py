from django import forms
from dblog.models import Article
class ArticleForm(forms.ModelForm):
 #post_article = forms.CharField(wiget=forms.Textarea)
 class Meta:
  model = Article
  fields = ['name', 'content']
