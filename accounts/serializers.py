from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user
    
# Login
class LoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username_or_email = data.get('username_or_email')
        password = data.get('password')

        user = None
        try:
            user = User.objects.get(username = username_or_email)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email = username_or_email)
            except User.DoesNotExist:
                pass
        if user:
            if user.check_password(password):
                if user.is_active:
                    return user
                else:
                    raise serializers.ValidationError("El usuario no está activo")
            else:
                raise serializers.ValidationError("Credenciales incorrectas")
        else:
            raise serializers.ValidationError("No se encontró un usuario con las creadenciales proporcionadas")