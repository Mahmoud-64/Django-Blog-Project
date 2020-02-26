from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from post import views as postview
from blog.views import index,blog,post
from landing_page import views as land_view

urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('post/', post),
    #post page
    path('post/<id>',land_view.post_page),
    #like page
    path('like/<u_id>/<p_id>',land_view.like),
    #dis like
    path('dislike/<u_id>/<p_id>',land_view.dislike),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)