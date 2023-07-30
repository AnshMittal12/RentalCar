from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.db import connection
from paynrentapp.serializers import AgencySerializers
from paynrentapp.models import Agency
from rest_framework.decorators import api_view 
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.

@api_view(['GET','POST','DELETE'])
def AdminLogin(request):
    return render(request,"LoginPage.html",{'message':''})


@api_view(['GET','POST','DELETE'])
def CheckAdminLogin(request):
    try:
        if request.method == 'GET':
            q = "select * from paynrentapp_administrator where (mobile_no='{0}' or email_id='{0}') and password='{1}'".format(request.GET['mobile_no'],request.GET['password'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print(record)
            if(len(record)==0):
                return render(request,"LoginPage.html",{'message':'Invalid Admin Id or Password'})
            else:
                return render(request,"DashBoard.html",{'data':record[0]}) 
            print("xxxxxxxxxx",record)
            
    except Exception as e:
        print("Error : ",e)
        return render(request,"LoginPage.html",{'data':[]})
    

@api_view(['GET','POST','DELETE'])
def AgencyLogin(request):
    return render(request,"AgencyloginPage.html",{'message':''})

@api_view(['GET','POST','DELETE'])
def AgencyData(request):
    if request.method == 'POST' :
        agency_serializer = AgencySerializers(data=request.data)
        if agency_serializer.is_valid():
            agency_serializer.save()
            return render(request,"AgencyloginPage.html",{"message":"Sign up sucessfull"})
        return render(request,"AgencyloginPage.html",{"message":"Failed"})
    
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
            if(len(record)==0):
                return render(request,"LoginPage.html",{'message':'Invalid Admin Id or Password'})
            else:
                return render(request,"DashBoard2.html",{'data':record[0]}) 
            print("xxxxxxxxxx",record)
            
    except Exception as e:
        print("Error : ",e)
        # return render(request,"Dashboard2.html",{'data':[]})

# xframe_options_exempt    
# @api_view(['GET','POST',])
# def DisplayAgency(request):
#     try:
#         if request.method == 'GET':
#             list_category = Agency.objects.all()
#             list_category_serializer = AgencySerializers(list_category,many=True)
#             records = tuple_to_dict.ParseDict(list_category_serializer.data)
#             return render(request,"AgencyDisplay.html",{'data':records})
#     except Exception as e:
#         print(e)
#         return render(request,"AgencyDisplay.html",{'data':{}})

# @xframe_options_exempt    
# @api_view(['GET','POST','DELETE'])
# def AgencyDelete(request):
#     try :
#         if request.method == 'GET' :
#             agency = Agency.objects.get(pk=request.GET['id'])
#             agency.delete()
#             return redirect('/api/displayagency')
#     except Exception as e:
#         print("Error :" ,e)
#         return redirect('/api/displayagency')       