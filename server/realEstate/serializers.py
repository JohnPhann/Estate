from rest_framework import serializers

from realEstate.models import HomeHire , HomeSale , homeHireUpload , homeSaleUpload , Host , Orientation , Role , Sale , Staff ,StateHire , StateSale , Customer , Categories





class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id','name']


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id','name','avatar','phone','email','city']

class CustomerSerializer(serializers.ModelSerializer):
    sale = SaleSerializer()
    class Meta:
        model = Customer
        fields = ['id','makh','name','phone','email','adress','street','ward','district','city','create_date','typeCustomer','sale','representativeName','phoneNDD']

class CustomerPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['name','phone','email','adress','street','ward','district','city','typeCustomer','sale','representativeName','phoneNDD','birthDate','cmnd','cmndDate','note','placeCmnd']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id','name']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id','name','avatar','phone','email','city','role']

class HostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Host
        fields = ['id','mahost','name','phone','create_date','email','adress','street','ward','district','city','typeHost','sale']

class HostPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Host
        fields = ['name','phone','email','adress','street','ward','district','city','typeHost','sale']

class OrientationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orientation
        fields = ['id','name']

class StateHireSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateHire
        fields = ['id','name']

class StateSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateSale
        fields = ['id','name']

class homeHireUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = homeHireUpload
        fields = ['id','picture']



class HomeHireSerializer(serializers.ModelSerializer):
    images = homeHireUploadSerializer(many=True , read_only = True)
    upload_images = serializers.ListField(
        child = serializers.ImageField(max_length=10000000 , allow_empty_file = False , use_url = False),
        write_only=True
    )

    def create(self , validated_data):
        upload_images = validated_data.pop("upload_images")
        new_picture = HomeHire.objects.create(**validated_data)
        for pic in upload_images:
            new_picture_image = homeHireUpload.objects.create(homeHire=new_picture , picture=pic)

        return new_picture
    

    class Meta:
        model = HomeHire
        fields = ['images','upload_images','adress','street','ward','district','city','area','saleablearea','floor','bedroom','wc','horizontal','lagreRoad','margin','price','commission','note','propose','categories','customer','host','orientation','sale','staff','stateHire','stateSale']

class homeSaleUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = homeSaleUpload
        fields = ['id','picture']

class HomeSaleSerializer(serializers.ModelSerializer):
    images = homeSaleUploadSerializer(many=True , read_only = True)
    upload_images = serializers.ListField(
        child = serializers.ImageField(max_length=10000000 , allow_empty_file = False , use_url = False),
        write_only=True
    )

    def create(self , validated_data):
        upload_images = validated_data.pop("upload_images")
        new_picture = HomeSale.objects.create(**validated_data)
        for pic in upload_images:
            new_picture_image = homeSaleUpload.objects.create(homeSale=new_picture , picture=pic)

        return new_picture
    

    class Meta:
        model = HomeSale
        fields = ['images','upload_images','adress','street','ward','district','city','area','saleablearea','floor','bedroom','wc','horizontal','lagreRoad','margin','price','commission','note','propose','categories','customer','host','orientation','sale','staff','stateHire','stateSale','altar','garden','packArea','pool','post_create_date','post_update_date','productOf','twoFace']

class HomeSaleGetSerializer(serializers.ModelSerializer):
    images = homeSaleUploadSerializer(many=True , read_only = True)
    categories = CategoriesSerializer()
    customer = CustomerSerializer()
    sale = SaleSerializer()
    staff = StaffSerializer()
    stateSale = StateSaleSerializer()
    stateHire = StateHireSerializer() 

    class Meta:
        model = HomeSale
        fields =  ['maBDS','images','adress','street','ward','district','city','area','saleablearea','floor','bedroom','wc','horizontal','lagreRoad','margin','price','commission','note','propose','categories','customer','host','orientation','sale','staff','stateHire','stateSale','altar','garden','packArea','pool','post_create_date','post_update_date','productOf','twoFace']