from django.shortcuts import render
from dblog.models import Article
from django.http import HttpResponse
from django.views.generic import TemplateView
from forms import ArticleForm

 
class HomeView(TemplateView):
  template_name = 'index.html'
def index(request):
 if request.method == 'GET':
        #latest_blog_list = Article.objects.all().order_by('-post_date')[:3]
        article = Article()
        form = ArticleForm()
        t = loader.get_template('blogproject/dblog/templates/index.html')
        c = Context({'form': form})
        return HttpResponse(t.render(c))
      if request.method == 'POST':
         form = ArticleForm(request.POST)
         if form.is_valid():
         return HttpResponseRedirect('/')
      else:
         form = ArticleForm()
         return render(request, 'index.html', {'form': form})
# Create your views here.
