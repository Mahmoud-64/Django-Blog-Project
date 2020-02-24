from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import index,blog,post
from post import views as postview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog),
    path('post/', post),
    path('admin_panel', postview.admin_panel_page),

    path('account/',include('accounts.urls')),
    #users_section
    path('admin/all_users',postview.all_users),
    path('admin/delete_user/<id>',postview.delete_user),
    path('admin/edit_user/<id>',postview.edit_user),
    path('admin/add_user',postview.add_user),
    #end user section 
    #blog section
    path('admin/addpost/', postview.add_post_view),
    path('admin/admin_posts_table/',postview.view_all_posts),
    path('admin/post_delete/<id>',postview.delete_posts),
    path('admin/editpost/<id>',postview.edit_post),
    #end blog section


    #tags_section
    path('tags', postview.tags),
    path('add_tag',postview.add_tag),
    path('del_tag/<id>',postview.del_tag),
    path('edit_tag/<id>',postview.edit_tag),

    #category_section
    path('categories', postview.category),
    path('add_cat',postview.add_cat),
    path('edit_cat/<id>',postview.edit_cat),
    path('del_cat/<id>',postview.del_cat),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
