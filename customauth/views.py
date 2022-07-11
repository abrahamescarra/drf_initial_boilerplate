from rest_framework import generics,permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from datetime import timedelta
from DRFBoilerPlate.local_settings import ALLOWED_IP
from rest_framework import status

class RegisterAPI(generics.GenericAPIView):
    serializer_class=RegisterSerializer

    def post(self, request,*args,**kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
        })

        #ip = request.META['REMOTE_ADDR']
        # if ip in ALLOWED_IP:
        #     
        # else: 
        #     return Response(status=status.HTTP_403_FORBIDDEN)
       

class LoginAPI(generics.GenericAPIView):
    serializer_class=LoginSerializer

    def post(self, request,*args,**kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data
        if request.data.get('remember'):
            return Response({
                "user": UserSerializer(user,context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user,expiry=timedelta(hours=24))[1]
            })
        else:   
            return Response({
                "user": UserSerializer(user,context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1]
            })
            
        

class UserAPI(generics.RetrieveAPIView):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class UserUpdateAPI(generics.UpdateAPIView):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class ChangePasswordView(generics.UpdateAPIView):

    
    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user