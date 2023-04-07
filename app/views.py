from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.
def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='cricket')
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    LOW=Webpage.objects.all().order_by
    LOW=Webpage.objects.exclude(topic_name='cricket')
    d={'webpages':LOW}
    return render(request,'display_webpages.html',context=d)

def display_accessrecords(request):
    LOA=Accessrecord.objects.all()
    LOA=Accessrecord.objects.filter(date__gt='2023-04-02')
    d={'accessrecords':LOA}
    return render(request,'display_accessrecords.html',context=d)

