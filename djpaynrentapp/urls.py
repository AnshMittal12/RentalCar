"""djpaynrentapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from paynrentapp import category_view
from paynrentapp import subcategory_view
from paynrentapp import vehicle_view
from paynrentapp import admin_login
from paynrentapp import user_view
from paynrentapp import agency_vehicle_view

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/categoryinterface',category_view.CategoryInterface),
    re_path(r'^api/categorysubmit',category_view.CategorySubmit),
    re_path(r'^api/displaycategory',category_view.DisplayCategory),
    re_path(r'^api/display_category_by_id',category_view.DisplayByCategoryId),
    re_path(r'^api/editcategory',category_view.EditCategory),
    re_path(r'^api/category_icon_display',category_view.DisplayCategoryIcon),
    re_path(r'^api/category_save_icon',category_view.Category_Save_Icon),
    re_path(r'^api/jsondisplaycategory',category_view.DisplayCategoryJSON),

    re_path(r'^api/subcategoryinterface',subcategory_view.SubCategoryInterface),
    re_path(r'^api/subcategorysubmit/&',subcategory_view.SubCategorySubmit),
    re_path(r'^api/displaysubcategory',subcategory_view.DisplaySubCategory),
    re_path(r'^api/subcategorydisplaybyid',subcategory_view.DisplaySubCategorybyId),
    re_path(r'^api/editsubcategory',subcategory_view.EditSubCategory),
    re_path(r'^api/subcategoryicondisplay',subcategory_view.DisplaySubCategoryIcon),
    re_path(r'^api/savesubcategoryicon',subcategory_view.SubCategoryIconSave),
    re_path(r'^api/jsonsubcategorydisplaybyid',subcategory_view.DisplaySubCategorybyIdJSON),
    
    re_path(r'^api/vehicleinterface',vehicle_view.VehicleInterface),
    re_path(r'^api/vehiclesubmit',vehicle_view.VehicleSubmit),
    re_path(r'^api/vehicledisplay',vehicle_view.VehicleDisplay),
    re_path(r'^api/displayvehiclebyid',vehicle_view.VehicleDisplayById),
    re_path(r'^api/editvehicle',vehicle_view.EditVehicle),
    re_path(r'^api/vehicleicondisplay',vehicle_view.DisplayVehicleIcon),
    re_path(r'^api/savevehicleicon',vehicle_view.SaveVehicleIcon),

    re_path(r'^api/loginpage',admin_login.AdminLogin),
    re_path(r'^api/checkadminlogin',admin_login.CheckAdminLogin),
    re_path(r'^api/agencyloginpage',admin_login.AgencyLogin),
    re_path(r'^api/agencysubmit',admin_login.AgencyData),
    
    re_path(r'^api/index',user_view.Index),
    re_path(r'^api/displayvehicleforuser',user_view.VehicleDisplayForUser),
    re_path(r'^api/uservehiclelist',user_view.UserVehiclePage),
    re_path(r'^api/displayselectedvehicle',user_view.DisplaySelectedVehicle),
    re_path(r'^api/showvehiclelist',user_view.ShowVehicleList),
    re_path(r'^api/pagetwoshowvehiclelist',user_view.ShowVehicleListPage2),
    re_path(r'^api/setmobileandemail',user_view.SetMobileandEmail),
    re_path(r'^api/userloginsignup',user_view.UserLoginSignup),
    re_path(r'^api/submituserdata',user_view.UsersData),
    re_path(r'^api/checkuserlogin',user_view.CheckUserLogin),


    re_path(r'^api/agencychecklogin',agency_vehicle_view.CheckAgencyLogin),
    re_path(r'^api/agencyvehicledisplay',agency_vehicle_view.AgencyVehicleDisplay),
    re_path(r'^api/agencyinterface',agency_vehicle_view.AgencyInterface),
    re_path(r'^api/agencyvehiclesubmit',agency_vehicle_view.AgencyvehicleSubmit),
    re_path(r'^api/agencyDelete', agency_vehicle_view.DeleteAgencyVehicle),
    re_path(r'^api/displayagency', agency_vehicle_view.DisplayAgency),
    re_path(r'^api/deleteagency', agency_vehicle_view.AgencyDelete),
    
]
