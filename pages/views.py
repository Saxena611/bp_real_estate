from django.shortcuts import render
from realtors.models import Realtor
from listings.models import Listing
from areaprops.models import Area 
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    areas = Area.objects.order_by('-area_name')
    context = {
        "listings":listings,
        'arealist':areas
    }
    print(context)
    return render(request,'pages/index.html',context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    areas = Area.objects.order_by('-area_name')
    context = {
        "realtors":realtors,
        "mvp_realtors":mvp_realtors,
        'arealist':areas
    }
    return render(request,'pages/about.html',context)

def propertyin(request,area_id):
    property_in = Listing.objects.filter(area=area_id)
    areas = Area.objects.order_by('-area_name')
    paginator = Paginator(property_in,2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings':paged_listings,
        'arealist':areas
    }
    
    return render(request,'listings/listings.html',context)