from django.urls import path
from . import views
from myapp.views import CustomLoginView, CustomLogoutView, CustomUserCreationView

urlpatterns = [

     path('login/',views.custom_login,name='login'),
     path('logout/',views.custom_logout,name='logout'),
     #path('login/', CustomLoginView.as_view(), name='login'),
     #path('logout/', CustomLogoutView.as_view(), name='logout'),
     path('register/', CustomUserCreationView.as_view(), name='register'),
     path('',views.newhome,name = 'newhome'),     
     path('filtered_table_view/',views.filtered_table_view,name = 'filtered_table_view'),                
     path('filtered_table/', views.filtered_table, name='filtered_table'),
     path('home/',views.home,name = 'home'),
     #path('login/',views.login,name='login'), #old login
     #path('api/userlogin/',views.userLogin,name='userlogin'),
     path('api/filterapi/',views.filterAPI,name='filterapi'),

 ]



 