from django.urls import path , include
from .views import HelloAPIView
from .views import UserAuthenticationAPIView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoriesViewSet)
router.register(r'role', views.RoleViewSet)
router.register(r'sale', views.SaleViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'host', views.HostViewSet)
router.register(r'staff', views.StaffViewSet)
router.register(r'orientation', views.OrientationViewSet)
router.register(r'stateHire', views.StateHireViewSet)
router.register(r'stateSale', views.StateSaleViewSet)
router.register(r'homeSale', views.HomeSaleViewSet)
router.register(r'homeHire', views.HomeHireViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', HelloAPIView.as_view(), name='hello'),
    path('user-authentication/', UserAuthenticationAPIView.as_view(), name='authentication'),

   
]