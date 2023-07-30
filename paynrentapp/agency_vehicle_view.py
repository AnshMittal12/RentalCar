from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
from rest_framework.decorators import api_view
from paynrentapp.serializers import VehicleSerializers
from paynrentapp.models import Vehicle
from paynrentapp.models import Agency
from paynrentapp.serializers import AgencySerializers
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def AgencyInterface(request):
   
        q = " select * from paynrentapp_agency where id = {0}".format(v)
        print(q)
        cursor = connection.cursor()
        cursor.execute(q)
        records = tuple_to_dict.ParseDictMultipleRecord(cursor)
        print("xxxxxxxxxx",records)
        return render(request,"AgencyInterface.html",{'data':records[0]})

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def AgencyvehicleSubmit(request):
    if request.method == 'POST':
        vehicle_serializers = VehicleSerializers(data=request.data)
        if vehicle_serializers.is_valid():
            vehicle_serializers.save()
            return render(request,"AgencyInterface.html",{'message':"Record Submitted Sucessfully"})
        return render(request,"AgencyInterface.html",{'message':"Fail to Submit Record"})
    

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def AgencyVehicleDisplay(request):
    try:
        if request.method == 'GET':     
            q = "select * from paynrentapp_agency where (mobile_no='{0}' or email_id='{0}') and password='{1}'".format(request.GET['mobile_no'],request.GET['password'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            if(record): 
                print(record)
                print(record[0])
                global v
                v = record[0]['id']
                print("hullaaaa",v)
                # list_vehicle = Vehicle.objects.all()
                # list_vehicle_serializers = VehicleSerializers(list_vehicle,many=True)
                # records = tuple_to_dict.ParseDict(list_vehicle_serializers.data)    
                q = " select V.*,( select C.categoryname from paynrentapp_category C where C.id = V.category_id) as categoryname,( select A.agency_name from paynrentapp_agency A where A.id = V.agency_id) as agency_name, ( select S.subcategory_name from paynrentapp_subcategory S where S.id = V.subcategory_id) as subcategory_name from paynrentapp_vehicle V where V.agency_id = {0}".format(v)
                print(q)
                cursor = connection.cursor()
                cursor.execute(q)
                records = tuple_to_dict.ParseDictMultipleRecord(cursor)
                print("xxxxxxxxxx",records)
                return render(request,"AgencyVehicleDisplay.html",{'data':records})
            else:
                return render(request,"AgencyloginPage.html",{'message':'NO record Found'})
    except Exception as e:
        print("Error : " ,e)
        return render(request,"AgencyVehicleDisplay.html",{'data':{}})  
    
@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def DeleteAgencyVehicle(request):
    try :
        if request.method == 'GET' :
            vehicle = Vehicle.objects.get(pk=request.GET['id'])
            vehicle.delete()
            return redirect('/api/agencyvehicledisplay')
    except Exception as e:
        print("Error :" ,e)
        return redirect('/api/agencyvehicledisplay')
    
@api_view(['GET','POST','DELETE'])
def CheckAgencyLogin(request):
    try:
        if request.method == 'GET':
            q = "select * from paynrentapp_agency where (mobile_no='{0}' or email_id='{0}') and password='{1}'".format(request.GET['mobile_no'],request.GET['password'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print(record)
            print(record[0])
            global v
            v = record[0]['id']
            if(len(record[0])==0):
                return render(request,"LoginPage.html",{'message':'Invalid Admin Id or Password'})
            else:
                return render(request,"DashBoard2.html",{'data':record[0]}) 
            print("xxxxxxxxxx",record)
            
    except Exception as e:
        print("Error : ",e)
        # return render(request,"Dashboard2.html",{'data':[]})

@xframe_options_exempt    
@api_view(['GET','POST',])
def DisplayAgency(request):
    try:
        if request.method == 'GET':
            list_category = Agency.objects.all()
            list_category_serializer = AgencySerializers(list_category,many=True)
            records = tuple_to_dict.ParseDict(list_category_serializer.data)
            return render(request,"AgencyDisplay.html",{'data':records})
    except Exception as e:
        print(e)
        return render(request,"AgencyDisplay.html",{'data':{}})

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def AgencyDelete(request):
    try :
        if request.method == 'GET' :
            agency = Agency.objects.get(pk=request.GET['id'])
            agency.delete()
            return redirect('/api/displayagency')
    except Exception as e:
        print("Error :" ,e)
        return redirect('/api/displayagency') 