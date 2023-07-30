from rest_framework import serializers
from paynrentapp.models import Category
from paynrentapp.models import SubCategory
from paynrentapp.models import Vehicle
from paynrentapp.models import Administrator
from paynrentapp.models import Customer
from paynrentapp.models import Agency
from paynrentapp.models import User

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','categoryname','description','icon')

class SubCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id','category_id','company_name','subcategory_name','description','icon')

class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id','agency_id' ,'category_id','subcategory_id','city','model_year','variant','price','insured','registration_no','owner_name','mobile_no','color','fuel_type','no_of_seats','transmission_type','icon')

class AdministratorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('id','admin_name','email_id','mobile_no','password')

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','customerf_name',' customerl_name','email_id','mobile_no','password','address')

class AgencySerializers(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = ('id','agency_name','email_id','mobile_no','password')


class userserialiser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','Username','UserEmail','password','mobileno','start_date','end_date','duration')