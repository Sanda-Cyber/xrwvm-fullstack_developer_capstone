from django.urls import path  

 

from django.conf.urls.static import static  

 

from django.conf import settings  

 

from djangoapp.views import login_user   

from . import views 


 

 

  

 

app_name = 'djangoapp'  

 

urlpatterns = [  

    path('logout/', views.logout_request, name='logout'), 
 

    # # path for registration  
    path('register/', views.register_view, name='register'),

 

  

 

    # path for login  

 

    path('login/', login_user, name='login'),  

 

    # path(route='login', view=views.login_user, name='login'),  

    path(route='login', view=views.login_user, name='login'), 

     

 

  

 

    # path for dealer reviews view  

 

  

 

    # path for add a review view  

 

  

 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  

 