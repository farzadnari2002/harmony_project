from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    EmailField,
)
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    email = EmailField(allow_null=True)
    
    def validate_phone(self, phone):
        if len(phone)!=11:
            raise ValidationError('the phone number must be 11 digits long.')
        return phone
    
    
    class Meta:
        model = User
        fields = ['phone', 'password', 'email']
    

