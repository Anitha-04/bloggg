from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from blog.serializers import blogserializer
from blog.models import Postblog


def login(request):
    if request.method=='GET':
        return render(request, "login.html")
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        User = authenticate(request,username=username,password=password)
        if User is not None:
            return render(request,"blog1.html")
        else:
            return render(request, "login.html")

def register(request):
    if request.method=="GET":
        return render(request,'register.html')
    else:
        username= request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user( username=username,email=email,password=password)
        return render(request, "login.html")

def insertblog(request):
    if request.method=='GET':
        return render(request,"blog1.html")
    else:
        a = request.POST.get('date')
        b = request.POST.get('blog')
        Postblog.objects.create(date=a,blog=b)
        return render(request,"blog1.html")

@csrf_exempt
def blog1(request):
    if request.method=="GET":
        stud=Postblog.objects.all()
        serializer=blogserializer(stud,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        data=JSONParser().parse(request)
        serializer=blogserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@api_view(['GET','PUT','DELETE'])
def blog2(request,pk):
    try:
        blogg=Postblog.objects.get(pk=pk)
    except blogg.DoesNotExist:
        return HttpResponse(status=404)
    if request.method=='GET':
        serializer=blogserializer(blogg)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer=blogserializer(blogg,data=data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method=='DELETE':
        blogg.delete()
        return HttpResponse(status=204)
