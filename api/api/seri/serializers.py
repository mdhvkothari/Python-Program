from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    rollno = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)


class StudentDeserializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    rollno = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)



class StudentUpdate(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    rollno = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

    def update(self,instance,validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.rollno = validate_data.get('rollno',instance.rollno)
        instance.city = validate_data.get('city',instance.city)

        instance.save()
        return  instance