from django.shortcuts import render

def index(request):
    return render(request, "index_start.html")

# def multi_language(request):
#     return render(request,"multi_language.html")

# Create your views here.
