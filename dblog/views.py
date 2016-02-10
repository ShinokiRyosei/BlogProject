from django.shortcuts import render, get_object_or_404
from dblog.models import Article
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from forms import ArticleForm, LoginForm, SignupForm
from django.template import loader

 
class HomeView(TemplateView):
  template_name = 'index.html'
  context_object_name = 'latest_article_list'


class LoginView(TemplateView):
    template_name = 'login.html'


class SignupView(TemplateView):
    template_name = 'signup.html'


def index(request):
    latest_article_list = Article.objects.order_by('-post_date')[:5]
    template = loader.get_template('templates/index.html')
    context = {
        'latest_article_list': latest_article_list
    }
    return HttpResponse(template.render(context, request))


def post_article(request):
    form = ArticleForm()
    return render(request, 'index.html', {'form': form})


def login(request):
    form = LoginForm()
    return render(request, 'login.html',{'form': form})


def signup(request):
    form = SignupForm()
    return render(request, 'signup.html', {'form': form})
# Create your views here.
