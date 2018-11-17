from django.shortcuts import render,HttpResponse


# Create your views here.
def home(request):
    return render(request, 'Home/Home.html')


def contactus(request):
    return render(request, 'Home/ContactUs.html')


def aboutus(request):
    return render(request, 'Home/AboutUs.html')