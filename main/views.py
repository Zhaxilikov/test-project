from django.shortcuts import render
from news.models import Articles

from django.views.generic import DetailView
# from django.core.paginator import Paginator
# from django.views.generic import ListView




# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def index(request):
    news = Articles.objects.order_by('-data') [:4]
    return render(request, 'main/index.html', {'news': news})


    

    
# def articles(request, page_number = 1):
#     all_articles = Articles.objects.all()
#     page = Paginator(all_articles, 2)
#     return render(request, 'main/index.html', {'articles': page.page(page_number)})




class NewDetailView(DetailView):
    model = Articles
    template_name = 'index/Detail_View.html'
    context_object_name = 'article'





# class ContactListView(ListView):
#     paginate_by = 1
#     model = Articles


