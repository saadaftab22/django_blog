from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from users.views import UserViewSet, UserLogIn, RegisterUserAPIView, UserAPIView
from rest_framework.routers import DefaultRouter
from django.views.generic.base import RedirectView



router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    #path('api-user-login/', UserLogIn.as_view()),
    path('api/v1/', include(router.urls)),
    path('api-user-login/', UserLogIn.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-user-register/', RegisterUserAPIView.as_view()),
    path('profile/', UserAPIView.as_view()),

]