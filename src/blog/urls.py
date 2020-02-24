from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import index,blog,post
from post import views as postview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name ='post_list'),
    path('blog/', blog,),
    path('post/<id>/', post, name ='post_detail'),
    path('admin_panel', postview.admin_panel_page),

    path('account/',include('accounts.urls')),
    #users_section
    path('admin/all_users',postview.all_users),
    path('admin/delete_user/<id>',postview.delete_user),
    path('admin/edit_user/<id>',postview.edit_user),
    path('admin/add_user',postview.add_user),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
