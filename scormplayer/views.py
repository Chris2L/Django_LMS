from django.shortcuts import redirect, render


# Create your views here.
def index(request):
     return render(request,'index.html')
def index2(request):
     return render(request,'index2.html')
def apihtml(request):
     print("Returning api")
     return render(request,'api.html')
