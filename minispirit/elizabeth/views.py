from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def elizabeth(request):
    print(request.path_info.split('/').pop())
    return render(request,request.path_info.split('/').pop())
