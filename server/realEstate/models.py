from django.db import models
from server.utils import CustomAutoIncrementHireField , CustomAutoIncrementSaleField


# Create your models here.


class ItemBase(models.Model):
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Role(ItemBase):
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'role'

class Staff(ItemBase):
    name = models.CharField(max_length = 50 , null=False)
    avatar = models.ImageField(upload_to='uploads/%Y/%m' , blank=True , null=True)
    phone = models.IntegerField(null=False)
    email = models.CharField(max_length = 150 , null=False)
    city = models.CharField(max_length = 150 , null=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        db_table = 'staff'

class Sale(ItemBase):
    name = models.CharField(max_length = 50 , null=False)
    avatar = models.ImageField(upload_to='uploads/%Y/%m',blank=True , null=True)
    phone = models.IntegerField(null=False)
    email = models.CharField(max_length = 50 , null=False)
    city = models.CharField(max_length = 50 , null=False)

    class Meta:
        db_table = 'sale'

class Customer(ItemBase):
    makh = models.CharField(max_length = 150 ,unique=True , null=False)
    name = models.CharField(max_length = 50 , null=False)
    phone = models.CharField(null=False , max_length = 50)
    email = models.CharField(max_length = 50)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    adress = models.CharField(max_length = 50 , null=False)
    ward = models.CharField(max_length = 50 , null=False)
    district = models.CharField(max_length = 50 , null=False)
    city = models.CharField(max_length = 50 , null=False)
    street = models.CharField(max_length = 50 , null=False)
    typeCustomer = models.CharField(max_length = 50 , null=False)
    representativeName = models.CharField(max_length = 50 , null=True , blank=True)
    phoneNDD = models.CharField(max_length = 50 , null=True , blank=True)
    birthDate = models.DateField(blank=True,null=True)
    cmnd = models.CharField(max_length = 150,blank=True,null=True)
    cmndDate = models.DateField(blank=True,null=True)
    placeCmnd = models.CharField(max_length = 150 , null=True , blank=True)
    note = models.CharField(max_length = 250,null=True,blank=True)
    
    
    
    
    
    

    def save(self, *args, **kwargs):
        if not self.makh:
            customer = Customer.objects.order_by('-id').first()
            makh_id = customer.makh if customer else 'KH-0000000'
            new_makh_number = int(makh_id.split('-')[-1]) + 1     
            self.makh = f'KH-{str(new_makh_number).zfill(7)}'
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'customer'

class Host(ItemBase):
    mahost = models.CharField(max_length = 150 , unique=True)
    name = models.CharField(max_length = 50 , null=False)
    phone = models.IntegerField(null=False)
    email = models.CharField(max_length = 50)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    adress = models.CharField(max_length = 50 , null=False)
    street = models.CharField(max_length = 50 , null=False)
    ward = models.CharField(max_length = 50 , null=False)
    district = models.CharField(max_length = 50 , null=False)
    city = models.CharField(max_length = 50 , null=False)
    
    typeHost = models.CharField(max_length = 50 , null=False)

    def save(self, *args, **kwargs):
        if not self.mahost:
            host = Host.objects.order_by('-id').first()
            mahost_id = host.mahost if host else 'HOST-0000000'
            new_mahost_number = int(mahost_id.split('-')[-1]) + 1
            self.mahost = f'HOST-{str(new_mahost_number).zfill(7)}'
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'host'



class StateHire(ItemBase):
    name = models.CharField(max_length = 50 , null=False)

    class Meta:
        db_table = 'stateHire'

class StateSale(ItemBase):
    name = models.CharField(max_length = 50 , null=False)

    class Meta:
        db_table = 'stateSale'

class Orientation(ItemBase):
    name = models.CharField(max_length = 50 , null=False)

    class Meta:
        db_table = 'orientation'

class Categories(ItemBase):
    name = models.CharField(max_length = 50 , null=False)

    class Meta:
        db_table = 'categories'

class HomeSale(ItemBase):
    maBDS = models.CharField(max_length = 255 , unique=True)
    picture = models.ImageField(upload_to='uploads/%Y/%m',blank=True , null=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    adress = models.CharField(max_length = 150 , null=False)
    street = models.CharField(max_length = 150 , null=False)
    ward = models.CharField(max_length = 150 , null=False)
    district = models.CharField(max_length = 150 , null=False)
    city = models.CharField(max_length = 150 , null=False)
    area = models.IntegerField(null=False)
    saleablearea = models.IntegerField(null=False)
    orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE)
    floor = models.IntegerField(null=False)
    bedroom = models.IntegerField(null=False)
    wc = models.IntegerField(null=False)
    horizontal = models.IntegerField(null=False)
    lagreRoad = models.IntegerField(null=False)
    margin = models.IntegerField(null=False)
    price = models.BigIntegerField(null=False)
    stateSale = models.ForeignKey(StateSale, on_delete=models.CASCADE)
    stateHire = models.ForeignKey(StateHire, on_delete=models.CASCADE)
    commission = models.CharField(max_length = 150 , null=False)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    note = models.CharField(max_length = 150 , null=False)
    propose = models.CharField(max_length = 150 , null=False)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    post_create_date = models.DateField(blank=True,null=True)
    post_update_date = models.DateField(blank=True,null=True)
    productOf = models.CharField(max_length = 150 , blank=True,null=True)
    altar = models.BooleanField(blank=True ,null=True)
    garden = models.BooleanField(blank=True, null=True)
    packArea = models.BooleanField(blank=True, null=True)
    pool = models.BooleanField(blank=True, null=True)
    twoFace = models.BooleanField(blank=True, null=True)
    
    

    def save(self, *args, **kwargs):
        if not self.maBDS:
            homeSale = HomeSale.objects.order_by('-id').first()
            maBDS_id = homeSale.maBDS if homeSale else 'BDS-SALE-00000'
            new_maBDS_number = int(maBDS_id.split('-')[-1]) + 1
            self.maBDS = f'BDS-SALE-{str(new_maBDS_number).zfill(5)}'
        super().save(*args, **kwargs)


    class Meta:
        db_table = 'homeSale'

class homeSaleUpload(models.Model):
    homeSale = models.ForeignKey(HomeSale, on_delete=models.CASCADE , related_name="images")
    picture = models.ImageField(upload_to='uploads/%Y/%m' , null=True , blank=True)

    class Meta:
        db_table = 'homeSaleUpload'
    
    

class HomeHire(ItemBase):
    maBDS = models.CharField(max_length = 50 , unique=True)
    picture = models.ImageField(upload_to='uploads/%Y/%m',blank=True , null=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    adress = models.CharField(max_length = 150 , null=False)
    street = models.CharField(max_length = 150 , null=False)
    ward = models.CharField(max_length = 150 , null=False)
    district = models.CharField(max_length = 150 , null=False)
    city = models.CharField(max_length = 150 , null=False)
    area = models.IntegerField(null=False)
    saleablearea = models.IntegerField(null=False)
    orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE)
    floor = models.IntegerField(null=False)
    bedroom = models.IntegerField(null=False)
    wc = models.IntegerField(null=False)
    horizontal = models.IntegerField(null=False)
    lagreRoad = models.IntegerField(null=False)
    margin = models.IntegerField(null=False)
    price = models.BigIntegerField(null=False)
    stateSale = models.ForeignKey(StateSale, on_delete=models.CASCADE)
    stateHire = models.ForeignKey(StateHire, on_delete=models.CASCADE)
    commission = models.CharField(max_length = 150 , null=False)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    note = models.CharField(max_length = 150 , null=False)
    propose = models.CharField(max_length = 150 , null=False)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.maBDS:
            homeHire = HomeHire.objects.order_by('-id').first()
            maBDS_id = homeHire.maBDS if homeHire else 'BDS-HIRE-00000'
            new_maBDS_number = int(maBDS_id.split('-')[-1]) + 1
            self.maBDS = f'BDS-Hire-{str(new_maBDS_number).zfill(5)}'
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'homeHire'
    
class homeHireUpload(models.Model):
    homeHire = models.ForeignKey(HomeHire, on_delete=models.CASCADE , related_name="images")
    picture = models.ImageField(upload_to='uploads/%Y/%m',default="",null=True,blank=True)

    class Meta:
        db_table = 'homeHireUpload'   

    
    
    
    
    

    
    
    

    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    

