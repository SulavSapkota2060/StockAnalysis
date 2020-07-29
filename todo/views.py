from django.shortcuts import render

# Create your views here.


def tasks(request):
    return render(request,'todo/list.html')



def chart(request):
    return render(request,'todo/chart.html')