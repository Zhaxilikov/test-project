from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView

# Create your views here.

def news_home(request):
    news = Articles.objects.order_by('-data')
    return render(request, 'news/news_home.html', {'news': news})
    
    
def related(request):
    news = Articles.objects.order_by('-data')
    return render(request, 'news/related.html', {'news': news})


class NewDetailView(DetailView):
    model = Articles
    template_name = 'news/Detail_View.html'
    context_object_name = 'article'



