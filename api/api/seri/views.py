from django.shortcuts import render
from .models import Student
from .serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def student_views(request,pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type = 'applocation/json')
    #insted to using above two line we can use only one line
    return JsonResponse(serializer.data,safe=True)

def student_list(requeset):
    all = Student.objects.all()
    seril = StudentSerializer(all,many=True)
    # we use safe=False because this is non-dic type object
    return JsonResponse(seril.data,safe=False)

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json = request.body
        stream_data = io.BytesIO(json)
        parse_data = JSONParser().parse(stream_data)
        serializer = StudentDeserializer(data = parse_data)
        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Data Saved'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def student_update(request):
    if request.method == 'PUT':
        json = request.body
        strem_data = io.BytesIO(json)
        parse_data = JSONParser().parse(strem_data)
        id = parse_data.get('id')
        stu = Student.objects.get(id=id)
        #for patical update
        serializer = StudentUpdate(stu,data = parse_data,partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':"updated"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.error)
        return HttpResponse(json_data,content_type='application/json')


@csrf_exempt
def student_delete(request):
    if request.method == 'DELETE':
        json = request.body
        strem_data = io.BytesIO(json)
        parse_data = JSONParser().parse(strem_data)
        id = parse_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'Deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def student_filed_level_validate(request):
    if request.method == 'POST':
        json = request.body
        stream = io.BytesIO(json)
        parse_data = JSONParser().parse(stream)
        serializer = StudentValidation(data = parse_data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Data Saved'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
