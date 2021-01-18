from django.urls import path
from . import views

urlpatterns = [
    path('contact',views.contact,name='contact'),
    path('consulation',views.consulation,name='consulation'),
    path('postproperty',views.postproperty,name='postproperty'),
]