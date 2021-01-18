from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:area_id>',views.propertyin,name='propertyin'),
    path('about',views.about,name='about'),
]