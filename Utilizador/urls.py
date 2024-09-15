from django.urls import path
from . import views
from .views import UserLogout,UserLoginGerar1,UserCreateView,UserCreateView,UserListView,UserDeleteView,UserUpdateView


urlpatterns = [
   
   
    
    path('users/', views.list_users, name='list_users'),
    path('logingeral1/',  UserLoginGerar1.as_view(), name='user_logingeral'),
    path('logout/', UserLogout.as_view(), name='user-logout'),
    path('usercreate/', UserCreateView.as_view(), name='user-create'),
    path('userslist/', UserListView.as_view(), name='user-list'),
    path('userupdate/<int:pk>', UserUpdateView.as_view(), name='user-update'),
    path('userdelete/<int:pk>', UserDeleteView.as_view(), name='user-delete'),



    
    
]
