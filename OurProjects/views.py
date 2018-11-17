from django.shortcuts import render,HttpResponse


# Create your views here.
def ourprojects(request):
    return render(request, 'OurProjects/OurProjects.html')