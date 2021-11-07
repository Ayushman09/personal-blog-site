from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Contact


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})


def contact(request):
    if request.method == 'POST':
        contact_obj = Contact()
        name = request.POST.get('contactname')
        mail = request.POST.get('contactmail')
        msg = request.POST.get('contactmsg')
        contact_obj.cname = name
        contact_obj.cmail = mail
        contact_obj.cmsg = msg
        contact_obj.save()
        return render(request,'success.html')

    return render(request, 'contact.html')
