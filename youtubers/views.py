from django.shortcuts import render,get_object_or_404
from .models import Youtuber
# Create your views here.
def youtubers(request):
    tubers=Youtuber.objects.order_by('-created_data')
    data={
        'tubers':tubers
    }
    return render(request,'youtubers/youtubers.html',data)

def youtubers_details(request,id):
    youtuber=get_object_or_404(Youtuber,pk=id)
    data={
        'youtuber':youtuber
    }
    return render(request,'youtubers/youtubers_details.html',data)

def search(request):
    tubers=Youtuber.objects.order_by('-created_data')
    na=Youtuber.objects.values_list('name',flat=True).distinct()
    cts=Youtuber.objects.values_list('camera',flat=True).distinct()
    cats=Youtuber.objects.values_list('category',flat=True).distinct()

    if 'keyword'in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            tubers=tubers.filter(name__icontains=keyword)
    
    if 'name' in request.GET:
        name=request.GET['name']
        if name:
            tubers=tubers.filter(name__iexact=name)

    if 'category' in request.GET:
        category=request.GET['category']
        if category:
            tubers=tubers.filter(category__iexact=category)
    
    if 'camera_type' in request.GET:
        camera_type=request.GET['camera_type']
        if camera_type:
            tubers=tubers.filter(camera__iexact=camera_type)
    
    data={
        'tubers':tubers,
        'na':na,
        'cts':cts,
        'cats':cats,
    }
    return render(request,'youtubers/search.html',data)

