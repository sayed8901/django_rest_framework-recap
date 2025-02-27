from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    # to create student object
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    # to update student object
    def update(self, instance, validated_data):
        print('old data: ', instance.name, instance.roll, instance.city)

        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        print('updated: ', instance.name, instance.roll, instance.city)

        instance.save()

        return instance