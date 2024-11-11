from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()
     
        
class UserInfoSerializer(ModelSerializer):
    
    
    class Meta:
        model = User
        fields = ['phone', 'email', 'username']
        
        
class UserEditSerializer(ModelSerializer):
    
    
    class Meta:
        model = User
        fields = ['username', 'email']
