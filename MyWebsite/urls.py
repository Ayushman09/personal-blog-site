
from django.contrib import admin
from django.urls import path
from Blog import views as blog_views

urlpatterns = [
    path('contact/', blog_views.contact),
    path('', blog_views.index),
    path('admin/', admin.site.urls),
]
