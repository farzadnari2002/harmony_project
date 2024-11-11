from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
)
from ...models import Otp
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from ...utils import generate_otp


class LoginView(APIView):
    http_method_names = ['post']
    
    def post(self, request):
        phone = request.data.get('phone', '')
        try:
           user = User.objects.get(phone=phone)
           is_new = False
        except User.DoesNotExist:
            user = User.objects.create(phone=phone)
            is_new = True
            
        otp = generate_otp()
        Otp.objects.create(code=otp, user=user)
        
        response_data = {
            'is_new' : is_new,
            'otp' : otp,
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
    
    
class OtpVerifyView(APIView):
    http_method_names = ['post']
    
    def post(self, request):
        phone = request.data.get('phone', '')
        received_otp = request.data.get('otp', '')
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return Response({'error': 'User with this phone number does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        otp = user.get_last_otp()
        if received_otp == str(otp):
            refresh = RefreshToken.for_user(user)
            acces_token = str(refresh.access_token)
            
            return Response({
                'access_token':acces_token,
                'refresh_token':str(refresh)
            }, status=status.HTTP_200_OK)
            
        return Response({'error':'OTP code is wrong'}, status=status.HTTP_404_NOT_FOUND)
            
    
class UserInfoView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    
class UserEditView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserEditSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    
