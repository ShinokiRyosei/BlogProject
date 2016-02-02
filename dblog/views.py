from django.shortcuts import render

def index(request):
 latest_blog_list = Article.objects.all().order_by('-post_date')[:3]
 return render_to_response('templates/index.html', {'latest_blog_list' : lastest_blog_list})
# Create your views here.
