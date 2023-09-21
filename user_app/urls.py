from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, register
from django.contrib.auth.views import LoginView, LogoutView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='user_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]
urlpatterns += router.urls
