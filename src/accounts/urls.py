from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf import settings
from .views import signup_view,login_view,add_post_view,view_all_posts,delete_posts,edit_post

urlpatterns = [
    path('signup/', signup_view),
    path('login/', login_view),
    path('addpost/', add_post_view),
    path('admin_posts_table/',view_all_posts),
    path('post_delete/<id>',delete_posts),
    path('editpost/<id>',edit_post),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
