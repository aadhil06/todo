from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.user_signup,name='signup'),
    path('login',views.user_login,name='login'),
    path('index',views.index,name='index'),
    path('update_task/<str:pk>/',views.update_task,name='update'),
    path('delete_task/<str:pk>/',views.delete_task,name='delete'),
    path('logout',views.user_logout,name='logout') 
    
    
]
