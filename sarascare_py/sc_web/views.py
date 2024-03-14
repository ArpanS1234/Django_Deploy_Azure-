from django.shortcuts import render

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

def contactus(request):
    return render(request, 'sc_web/contact-us.html')

def donate(request):
    return render(request, 'sc_web/donate.html')

def pagenotfound(request):
    return render(request, 'sc_web/404.html')