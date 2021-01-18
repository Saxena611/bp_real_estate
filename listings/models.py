from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
from realtors.models import Realtor
from areaprops.models import Area

# Create your models here

# Choices for amenities
amenities_choices = (
    ('security','security'),
    ('gymnasium','gymnasium'),
    ('waste disposal','waste disposal'),
    ('reserved parking','reserved_parking'),
    ('lift','lift'),
    ('club house','club house'),
    ('shopping center','shopping center'),
    ('rain water harvesting','rain water harvesting'),
    ('water plant','water plant'),
    ('landscape garden','landscape garden'),
    ('kids play area','kids play area'),
    ('cctv','cctv'),
    ('cycle track','cycle track')
)


# Type of property
type_of_property = (
    ("1/2/3 BHK APARTMENT","1/2/3 BHK APARTMENT"),
    ("1/2 BHK APARTMENT","1/2 BHK APARTMENT"),
    ("1 BHK APARTMENT","1 BHK APARTMENT"),
    ("2 BHK APARTMENT","2 BHK APARTMENT"),
    ("3 BHK APARTMENT","3 BHK APARTMENT"),
    ("3 BHK DUPLEX","3 BHK DUPLEX"),
    ("2 BHK DUPLEX","2 BHK DUPLEX"),
    ("VILLA","VILLA"),
    ("BUNGALOW","BUNGALOW"),
    ("PLOT","PLOT"),
    ("PENTHOUSE","PENTHOUSE")
)

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    builder = models.CharField(max_length=200)
    rera_id = models.CharField(max_length=200)
    project_id = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    city = models.CharField(max_length=30,default='bhopal')
    state = models.CharField(max_length=30,default='MP')
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    amenities = MultiSelectField(choices=amenities_choices)
    price_start = models.IntegerField()
    price_end = models.IntegerField()
    area_start = models.IntegerField()
    area_end = models.IntegerField()
    property_type = models.CharField(max_length=30,choices=type_of_property)
    possesion = models.CharField(max_length=20)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title