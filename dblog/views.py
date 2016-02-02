from django.shortcuts import render
from dblog.models import Article
from django.http import HttpResponse
from django.views.generic import TemplateView
#from dblog.forms import ArticleForm

 
class HomeView(TemplateView):
  template_name = 'index.html'
def index(request):
        #latest_blog_list = Article.objects.all().order_by('-post_date')[:3]
       # article = Article()
      #  t = loader.get_template('blogproject/templates/index.html')
     #   c = Context({})
        return HttpResponse(t.render(c))
      if request.method == 'POST':
         form = ArticleForm(request.POST)
         if form.is_valid():
         return HttpResponseRedirect('/')
      else:
         form = ArticleForm()
         return render(request, 'index.html', {'form': form})
# Create your views here.
