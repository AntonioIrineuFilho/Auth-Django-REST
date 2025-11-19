from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioAuthViewSet

router = DefaultRouter()
router.register(r'auth', UsuarioAuthViewSet, basename='auth')

urlpatterns = router.urls