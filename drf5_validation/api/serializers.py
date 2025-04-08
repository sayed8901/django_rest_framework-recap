from rest_framework import serializers
from .models import Student



# reusable custom validator
def can_contain_alphabet_only(value):
    if not value.isalpha():
        raise serializers.ValidationError(
            "This field must contain alphabets only. Numbers and special characters are not allowed."
        )


# student serializer class
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[can_contain_alphabet_only])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100, validators=[can_contain_alphabet_only])

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
    

    # field level validation implementation for the 'roll' field
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value


    # object level validation
    def validate(self, data):
        name = data['name']     # or, data.get('name')
        city = data['city']     # or, data.get('city')

        if name.lower() == "sohel" and city.lower() != "dhaka":
            raise serializers.ValidationError("City must be Dhaka")
    
        return data

