from django.shortcuts import render
from .models import Listing
from areaprops.models import Area 
from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .forms import ListingForm
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    areas = Area.objects.order_by('-area_name')
    paginator = Paginator(listings,10)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings':paged_listings,
        'arealist':areas
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    areas = Area.objects.order_by('-area_name')
    context = {
        'listing':listing,
        'arealist':areas
    }
    return render(request,'listings/listing.html',context)

def search(request):
    return render(request,'listings/search.html')

def postproperty(request):
    prop =  ListingForm()
    return render(request,'listings/postproperty.html',{'form':prop})