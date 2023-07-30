from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.db import connection
from rest_framework.decorators import api_view
from paynrentapp.serializers import userserialiser
from paynrentapp.models import User
from . import tuple_to_dict
import json
import datetime


@api_view(['GET', 'POST', 'DELETE'])
def Index(request):
    return render(request, "Index.html", {'message': ''})


@api_view(['GET', 'POST', 'DELETE'])
def ShowVehicleList(request):
    userdata = {'mobile_no': '','email_address' : '' , 'city': request.GET['city'], 'start_date': request.GET['start_date'],'end_date': request.GET['end_date'], 'days': request.GET['dh']}
    request.session["USERDATA"] = userdata
    return JsonResponse(userdata, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def ShowVehicleListPage2(request):
    userdata = request.session["USERDATA"]
    userdata['city'] = request.GET['city']
    userdata['start_date'] = request.GET['start_date']
    userdata['end_date'] = request.GET['end_date']
    userdata['days'] = request.GET['days']
    request.session["USERDATA"] = userdata
    print("Dayyysss :",userdata['days'])
    return JsonResponse(userdata, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def UserVehiclePage(request):
    userdata = request.session["USERDATA"]
    # userdata['city'] = request.GET['city']
    # userdata['start_date'] = request.GET['start_date']
    # userdata['end_date'] = request.GET['end_date']
    # userdata['days'] = request.GET['days']
    # request.session["USERDATA"] = userdata
    print("UuUUssser", userdata)
    return render(request, "UserVehicleList.html", {'userdata': userdata})

@api_view(['GET','POST','DELETE'])
def SetMobileandEmail(request):
   
    # print("AAAAAAAAAAAAAA" ,request.sessions['USERDATA'])
    userdata = request.session['USERDATA']
    print("MEWMEWMEW yyyyyyyyyyyyyyyyy",userdata['city'])
    userdata['name'] = request.GET['name']
    userdata['mobile_no'] = request.GET['mobile_no']
    userdata['email_address'] = request.GET['email_address']
    request.session['USERDATA'] = userdata 
    print("AAAAAAAAAAAAAA" ,userdata)
    return JsonResponse(userdata, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def DisplaySelectedVehicle(request):
    vehicle = request.GET['vehicle']
    selected_vehicle = json.loads(vehicle)
    print("XXXXXXXXXXXXX--------", selected_vehicle)
    userdata = request.session["USERDATA"]
    st = datetime.datetime.strptime(userdata['start_date'], "%Y/%m/%d %H:%M")
    et = datetime.datetime.strptime(userdata['end_date'], "%Y/%m/%d %H:%M")
    userdata['start_date'] = datetime.datetime.strftime(st, "%a %d %b %Y")
    userdata['end_date'] = datetime.datetime.strftime(et, "%a %d %b %Y")
    # print("Dayyysss :",userdata['days'])
    d = userdata['days'].split(":")
    userdata['days'] = d[0] + " Days , " + d[1] + " Hours"
    userdata['fare'] = selected_vehicle['price']
    hr = int(selected_vehicle['price'])//24
    userdata['amount'] = int(d[0])*int(selected_vehicle['price'])+(hr*int(d[1]))
    userdata['netamount'] = userdata['amount'] + 600 + 600
    return render(request, "DisplaySelectedVehicle.html", {'vehicle': selected_vehicle, 'userdata': userdata})


@api_view(['GET', 'POST', 'DELETE'])
def VehicleDisplayForUser(request):
    try:
        if request.method == 'GET':
            userdata = request.session["USERDATA"]
            # list_vehicle = Vehicle.objects.all()
            # list_vehicle_serializers = VehicleSerializers(list_vehicle,many=True)
            # records = tuple_to_dict.ParseDict(list_vehicle_serializers.data)
            if request.GET['param'] == "all":
                q = " select V.*,( select C.categoryname from paynrentapp_category C where C.id = V.category_id) as categoryname, ( select S.subcategory_name from paynrentapp_subcategory S where S.id = V.subcategory_id) as subcategory_name , ( select S.company_name from paynrentapp_subcategory S where S.id = V.subcategory_id) as company_name from paynrentapp_vehicle V where city='{0}'".format(userdata['city'])
            else:
                q = " select V.*,( select C.categoryname from paynrentapp_category C where C.id = V.category_id) as categoryname, ( select S.subcategory_name from paynrentapp_subcategory S where S.id = V.subcategory_id) as subcategory_name , ( select S.company_name from paynrentapp_subcategory S where S.id = V.subcategory_id) as company_name from paynrentapp_vehicle V where V.subcategory_id in (select id from paynrentapp_subcategory where company_name in ({}) or fuel_type in ({}) or transmission_type in ({}))".format(request.GET['param'],request.GET['param'],request.GET['param'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print("xxxxxxxxxx", records)
            return JsonResponse(records, safe=False)
    except Exception as e:
        print("Error : ", e)
        return JsonResponse(records, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def UserLoginSignup(request):
    userdata = request.session["USERDATA"]
    return render(request, "UserLoginSignup.html", {'message': '','userdata': userdata})

   
@api_view(['GET','POST','DELETE']) 
def UsersData(req):
    if req.method == 'POST':
        us_srlsr = userserialiser(data=req.data)
        print(req.data)
        print(us_srlsr)
        try:
            if us_srlsr.is_valid():
                us_srlsr.save()
                return render(req,"UserLoginSignup.html",{"message":"Data saved"})
            return render(req,"UserLoginSignup.html",{"message":"Failed"})

        except Exception as e:
            print("Error",e)
            return render(req,"UserLoginSignup.html",{"message":"Failed"})

    return render(req,"UserLoginSignup.html")


@api_view(['GET','POST','DELETE'])
def CheckUserLogin(request):
    try:
        print("HI")
        userdata = request.session["USERDATA"]
        print("HI")
        # amt = userdata['amount']
        # client = razorpay.Client(auth=(settings.KEY,settings.SECRET))
        # payment = client.order.create({'amounttt':amt,'currency':'INR'})
        # context = {'payment': payment}
        # print(payment)
        if request.method == 'GET':
            q = "select * from paynrentapp_user where mobileno='{0}' and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            if(record):

                print(record)
                print("dscdhfaydcsvyc",record[0]['id'])
                return render(request,"UserLoginSignup.html",{'message':'Data Matched','userdata':userdata})
            else:
                return render(request,"UserLoginSignup.html", {'message':'Invalid Id or pass'})
            
    except Exception as e:
        print("Error : ",e)
        # return render(request,"Dashboard.html",{'data':[],'status':False})