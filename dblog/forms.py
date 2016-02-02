from django.forms import ModelForm
from dblog.models import Article
class ArticleForm(ModelForm):
 #post_article = forms.CharField(wiget=forms.Textarea)
 class Meta:
  model = Book
  fields = ('name', 'content')
