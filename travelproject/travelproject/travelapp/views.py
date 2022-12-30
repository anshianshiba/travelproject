from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from . models import place
from . models import team

def demo(request):
    obj = place.objects.all()
    obj1 = team.objects.all()
    return render(request,'index.html',{'result':obj, 'team':obj1})

#def about(request):
#    name = "About"
#    return render(request,'about.html',{'obj':name})
#def contact(request):
#    return HttpResponse("Hello its contact page")
#def addition(request):
#    x = int(request.GET['num1'])
#    y = int(request.GET['num2'])
#    res = x + y
#    return render(request,'result.html',{'result':res})