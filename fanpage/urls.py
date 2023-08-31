from django.contrib import admin
from django.urls import path
import fanpageapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fanpageapp.views.firstpage, name='firstpage'),
    path('main/', fanpageapp.views.main, name='main'),
    path('gallery/', fanpageapp.views.gallery, name='gallery'),  
    path('community/', fanpageapp.views.community, name='community'),  
]
