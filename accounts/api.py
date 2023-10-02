from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework import status

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            _, token = AuthToken.objects.create(user)

            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": token
            })
        except Exception as e:
            return Response({'msg': str(e)}, status=e.status_code)

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data
            _, token = AuthToken.objects.create(user)

            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": token
            })
        except Exception as e:
            return Response({'msg': str(e)}, status=e.status_code)
            
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
class TokenRefresh(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    
    def get (self, request):
        user = request.user
        _, token = AuthToken.objects.create(user)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token
        })
