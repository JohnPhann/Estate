from rest_framework import viewsets , permissions
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.postgres.search import SearchVector
from realEstate.models import HomeHire , HomeSale , Host , Orientation , Role , Sale , Staff ,StateHire , StateSale , Customer , Categories
from realEstate.serializers import CategoriesSerializer , RoleSerializer , SaleSerializer , CustomerSerializer , StateHireSerializer , StateSaleSerializer , HomeHireSerializer , HomeSaleSerializer , StaffSerializer , HostSerializer , OrientationSerializer , CustomerPostSerializer , HostPostSerializer , HomeSaleGetSerializer




class HelloAPIView(APIView):
    def get(self, request):
        data = {'message': 'Hello, World!'}
        return Response(data)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategoriesSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name', '$phone']
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        else:
            return CustomerPostSerializer


class StateHireViewSet(viewsets.ModelViewSet):
    queryset = StateHire.objects.all()
    serializer_class = StateHireSerializer

class StateSaleViewSet(viewsets.ModelViewSet):
    queryset = StateSale.objects.all()
    serializer_class = StateSaleSerializer

class HomeHireViewSet(viewsets.ModelViewSet):
    queryset = HomeHire.objects.all()
    serializer_class = HomeHireSerializer

class HomeSaleViewSet(viewsets.ModelViewSet):
    queryset = HomeSale.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['adress', 'street','city','categories']
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HomeSaleGetSerializer
        else:
            return HomeSaleSerializer
    
    

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HostSerializer
        else:
            return HostPostSerializer

class OrientationViewSet(viewsets.ModelViewSet):
    queryset = Orientation.objects.all()
    serializer_class = OrientationSerializer


class UserAuthenticationAPIView(APIView):
    def post(self, request):
        # Perform authentication logic here
        # For example, validate username and password

        username = request.data.get('username')
        password = request.data.get('password')
        

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({'message': 'Authentication successful','login': True, 'access_token': str(refresh.access_token),'refresh_token': str(refresh),})
        else:
            return Response({'message': 'Invalid credentials','login': False})