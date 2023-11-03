from django.shortcuts import render

# Create your views here.
def index_view(request):
    context={
        "first_name":"mohammad",
        "last_name":"askari",
        "age":"20",
        "email":"shayan.askari12345@gmail.com"
            }
    return render(request,'index.html',context)
#def inner_page(request):
#    return render(request,"inner-page.html")