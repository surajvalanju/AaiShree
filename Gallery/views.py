from django.http import HttpResponse,Http404
from .models import Gallery,OurProjects,OurProjectImages
from django.shortcuts import render,get_object_or_404


def gallery(request):
    all_OurProjects = OurProjects.objects.all()
    all_OurProjectImages = OurProjectImages.objects.get(pk=2)

    context = {
        'all_OurProjects': all_OurProjects,
        'all_OurProjectImages': all_OurProjectImages,
        'fk': 0,
    }

    return render(request,'Gallery/gallery.html', context)


def detail(request, image_id):
    #try:
       # gallery = Gallery.objects.get(pk=image_id)
   # except Gallery.DoesNotExist:
       # raise Http404("Image Does Not Exist")

    gallery = get_object_or_404(Gallery.imginfo_set.all,pk=image_id)
    return render(request,'Gallery/description.html', {'gallery': gallery})

