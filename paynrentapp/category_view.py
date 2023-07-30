from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.db import connection
from rest_framework.decorators import api_view 
from paynrentapp.serializers import CategorySerializers
from paynrentapp.models import Category
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt
import os

# Create your views here.

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def CategoryInterface(request):
    return render(request,"CategoryInterface.html")

@xframe_options_exempt
@api_view(['GET','POST'])
def CategorySubmit(request):
    if request.method == 'POST':
        category_serializer = CategorySerializers(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return render(request,"CategoryInterface.html",{"message":"Record Submitted Sucessfully"})
        return render(request,"CategoryInterface.html",{"message":"Fails to Submit Record"})

@xframe_options_exempt    
@api_view(['GET','POST',])
def DisplayCategory(request):
    try:
        if request.method == 'GET':
            list_category = Category.objects.all()
            list_category_serializer = CategorySerializers(list_category,many=True)
            records = tuple_to_dict.ParseDict(list_category_serializer.data)
            return render(request,"CategoryDisplay.html",{'data':records})
    except Exception as e:
        print(e)
        return render(request,"CategoryDisplay.html",{'data':{}})

@xframe_options_exempt
@api_view(['GET','POST',])
def DisplayByCategoryId(request):
    try:
        if request.method == 'GET':
            q="select * from paynrentapp_category where id={0}".format(request.GET['id'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictSingleRecord(cursor)
            print("xxxxxxxx",record)
            return render(request,"DisplayById.html",{'data':record})
    except Exception as e:
        print("12345")
        print(e)
        return render(request,"DisplayById.html",{'data':{}})
    
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def EditCategory(request):
    try:
        if request.method == 'GET':
            if request.GET['btn'] == 'Edit' :   
                category = Category.objects.get(pk=request.GET['id'])
                category.categoryname = request.GET['categoryname']
                category.description = request.GET['description']
                category.save()
            else:
                category = Category.objects.get(pk=request.GET['id'])
                category.delete()
            return redirect('/api/displaycategory')
    except Exception as e:
        print("ERROR" , e)
        return redirect('/api/displaycategory')
    
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def DisplayCategoryIcon(request):
    try:
        if request.method == 'GET' :
            return render(request,"Display_Category_Icon.html",{'data':request.GET})
    except Exception as e:
        print("Error",e)
        return render(request,"Display_Category_Icon.html",{'data':[]})
    
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Category_Save_Icon(request):
    try:
        if request.method == 'POST':
            category = Category.objects.get(pk=request.POST['id'])
            category.icon = request.FILES['icon']
            category.save()
            os.remove('D:\DJANGO\djpaynrentapp\static/'+request.POST['oldpic'])
            return redirect('/api/displaycategory')
    except Exception as e:
        print("Error",e)
        return redirect('/api/displaycategory')
    
@xframe_options_exempt
@api_view(['GET','POST',])
def DisplayCategoryJSON(request):
    try:
        if request.method == 'GET':
            list_category = Category.objects.all()
            list_category_serializer = CategorySerializers(list_category,many=True)
            records = tuple_to_dict.ParseDict(list_category_serializer.data)
            return JsonResponse(data=records , safe=False)
    except Exception as e:
        print("Error :" ,e)
        return JsonResponse([],safe=False)
    
