from django.shortcuts import render

# Create your views here.
def Adm_index(request):
    return render(request, 'panelAdmin/Adm_index.html')

# POST
def post_index(request):
    return render(request, 'panelAdmin/include/post/post_index.html')
def post_created(request):
    return render(request, 'panelAdmin/include/post/post_created.html')
def post_edit(request):
    return render(request, 'panelAdmin/include/post/post_edit.html')
    


       