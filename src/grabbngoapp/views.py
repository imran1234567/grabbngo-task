from django.shortcuts import render

# Create your views here.

def grab_resturent_detail_view(request,id=1):
    return render(request,"grabbngoapp/detail_view.html",{})

def grab_resturent_list_view(request,id=1):
    return render(request,"grabbngoapp/list_view.html",{})


