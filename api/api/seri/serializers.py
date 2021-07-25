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


class StudentValidation(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    rollno = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

    #filed level validation
    def validate_rollno(self,value):
        if value >=200:
            raise serializers.ValidationError('Seat Full')
        return value


    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    #for multiple filed validation we use object validation
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        print(nm,ct)
        if nm.lower() == 'rohit' and ct.lower() != 'delhi':
            raise serializers.ValidationError('Name must not be rohit and city must be Noida')
        return data
    
    


# for model serializer
class modelSerializer(serializers.ModelSerializer):
    # we have to  implement meta method 
    # we have to method model that we want to serialize and then we have to mention fields 
    class Meta:
        model = Student
        fields = ['id','name','rollno','city']
        # now we don't use create and update that we used above it will provide automatically
        
    # below means when we update city or name then name will be same where we are updating or not
    # name = serializers.CharField(read_only=True)