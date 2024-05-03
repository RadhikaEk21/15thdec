from django.shortcuts import render
from django.http import HttpResponse
from student_app.models import Student

# Create your views here.
def sample_msg(request):
    return HttpResponse("hi response")



def register(request):
    if request.method=='POST':
        obj=Student()
        obj.Name=request.POST.get('n1')
        obj.Age=request.POST.get('a1')
        obj.Address=request.POST.get('ad1')
        obj.Gender=request.POST.get('g1')
        obj.Photo=request.POST.get('p1')
        obj.DOB=request.POST.get('d1')
        obj.save()
    return render(request,'register.html')

def view_reg(request):
    obj=Student.objects.all()
    return render(request,'view_reg.html',{'x':obj})




def delete_data(request,pk):
    obj=Student.objects.get(id=pk)
    obj.delete()
    return view_reg(request)


def update_data(request,pk):
    obj=Student.objects.get(id=pk)
    if request.method=='POST':
        obj=Student.objects.get(id=pk)
        obj.Name=request.POST.get('n1')
        obj.Age=request.POST.get('a1')
        obj.Address=request.POST.get('ad1')
        obj.Gender=request.POST.get('g1')
        obj.Photo=request.POST.get('p1')
        obj.DOB=request.POST.get('d1')
        obj.save()
        return view_reg(request)
    return render(request,'update_details.html',{'x':obj})

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import android_serializers


class student_view(APIView):
    def get(self,request):
        ob=Student.objects.all()
        ser=android_serializers(ob, many=True)
        return Response(ser.data)
    def post(self,request):
        ser=android_serializers(data=request.data)
        if ser.is_valid():
            ser.save()
        return  Response("ok") 