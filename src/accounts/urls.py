from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf import settings
from .views import *

urlpatterns = [
    path('signup/', signup_view),
    path('login/', login_view),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
