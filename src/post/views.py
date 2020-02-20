from django.shortcuts import render

# Create your views here.
#admin panel page
def admin_panel_page(request):
      return render(request,'admin panel/dashboard.html',{})
