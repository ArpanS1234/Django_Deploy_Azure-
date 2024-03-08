
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('causes/', views.causes, name='causes'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('contact-us/', views.contactus, name='contactus'),
    path('donate/', views.donate, name='donate'),
    path('404/', views.pagenotfound, name='404')
    # Add more paths as needed
]

