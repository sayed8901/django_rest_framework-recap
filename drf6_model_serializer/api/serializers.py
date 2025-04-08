from rest_framework import serializers
from .models import Student


# Custom validator
def can_contain_alphabet_only(value):
    if not value.isalpha():
        raise serializers.ValidationError(
            "This field must contain alphabets only. Numbers and special characters are not allowed."
        )
    

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, validators=[can_contain_alphabet_only]) 

    class Meta:
        model = Student
        fields = '__all__'

        read_only_fields = ['name']


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

