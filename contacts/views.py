from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact

# Create your views here.
def postproperty(request):
    if request.method == "POST":
        request_name = request.POST['request_name']
        request_id = 2
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if not request_name == "Post Property & Collaborate":
            request_name = "Post Property & Collaborate"
        
        contact = Contact(request=request_name,request_id=request_id,name=name,email=email,phone=phone,message=message)
        contact.save()
        
        messages.success(request,'Your request has been submitted, arealtor will get back to you soon.')
        
        return redirect('index')

    return

def contact(request):
    if request.method == "POST":
        request_name = request.POST['request_name']
        request_id = request.POST['request_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
    
        contact = Contact(request=request_name,request_id=request_id,name=name,email=email,phone=phone,message=message)
        contact.save()
        
        messages.success(request,'Your request has been submitted, arealtor will get back to you soon.')
        
        return redirect('index')
    
    return 

def consulation(request):
    if request.method == "POST":
        request_name = request.POST['request_name']
        request_id = 1
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if not request_name == "Free Property Consulation":
            request_name = "Free Property Consulation"
        
        contact = Contact(request=request_name,request_id=request_id,name=name,email=email,phone=phone,message=message)
        contact.save()
        
        messages.success(request,'Your request has been submitted, arealtor will get back to you soon.')
        
        return redirect('index')
    return 