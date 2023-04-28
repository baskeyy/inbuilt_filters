from django.shortcuts import render

# Create your views here.
def inbuilt_filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'hi HOW RE yOU','dt':dt}
    return render(request,'inbuilt_filters.html',d)