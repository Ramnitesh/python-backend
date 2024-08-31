"""
URL mappings for the user API.
"""
from django.urls import path
from user import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('auth/signin/', views.CreateTokenView.as_view(), name='signin'),
    path('auth/signout/', views.CreateTokenView.as_view(), name='signout'),
    path('token/delete/', views.CreateTokenView.as_view(), name='token-delete'),
    path('list/', views.UserViewSet.as_view({'get': 'list'}), name='list'),
    path('<int:pk>/', views.ManageUserView.as_view({'get': 'retrieve'}), name='detail'),
    path('<int:pk>/delete/', views.ManageUserView.as_view({'delete': 'destroy'}), name='delete'),
    path('<int:pk>/update/', views.ManageUserView.as_view({'put': 'update'}), name='update'),
]
