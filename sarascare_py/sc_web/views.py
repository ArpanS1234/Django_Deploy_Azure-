from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'sc_web/index.html')

def causes(request):
    return render(request, 'sc_web/causes.html')

def signup(request):
    return render(request, 'sc_web/signup.html')

def portfolio(request):
    return render(request, 'sc_web/portfolio.html')

def gallery(request):
    return render(request, 'sc_web/gallery.html')

def services(request):
    return render(request, 'sc_web/services.html')

def blog(request):
    return render(request, 'sc_web/blog.html')

def blog_1(request):
    return render(request, 'sc_web/blog-details.html')

def blog_2(request):
    return render(request, 'sc_web/blog_2.html')

def blog_3(request):
    return render(request, 'sc_web/blog_3.html')

def blog_4(request):
    return render(request, 'sc_web/blog_4.html')

def blog_5(request):
    return render(request, 'sc_web/blog_5.html')

def blog_6(request):
    return render(request, 'sc_web/blog_6.html')

def contactus(request):
    return render(request, 'sc_web/contact-us.html')

def donate(request):
    return render(request, 'sc_web/donate.html')

def pagenotfound(request):
    return render(request, 'sc_web/404.html')

