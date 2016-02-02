from django.shortcuts import render
from dblog.models import Article
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
  template_name = 'index.html'
def index(request):
        #latest_blog_list = Article.objects.all().order_by('-post_date')[:3]
        t = loader.get_template('blogproject/templates/index.html')
        c = Context({})
        return HttpResponse(t.render(c))
# Create your views here.
