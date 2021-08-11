from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.   

@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serilaizer = StudentSerializer(stu)
            return Response(serilaizer.data)    
        
        stu = Student.objects.all()
        serilaizer = StudentSerializer(stu,many = True)
        return Response(serilaizer.data)

    if request.method == 'POST':
        serilaizer = StudentSerializer(data = request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response({'msg':'Data Created'})
        return Response(serilaizer.error)
    
    if request.method == 'PUT':
        id = request.data.get('id')
        stu =  Student.objects.get(pk=id)
        serilaizer = StudentSerializer(stu,data = request.data,partial=True)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response({'msg':'Data Updated'})
        return Response(serilaizer.error)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Deleted'})






