from rest_framework import serializers
from .models import Account
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.hashers import check_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=60, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=60, write_only=True)

    class Meta:
        model = Account
        fields = ('username', 'role', 'password', 'password2')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError({'success': False, 'message': 'Password didn\'t match, please try again'})
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        return Account.objects.create_user(**validated_data)

    def validate_username(self, value):
        if not value.isalnum():
            raise serializers.ValidationError('Username must contain only alphanumeric characters and underscores.')
        if value[0].isdigit():
            raise serializers.ValidationError('Username must start with a letter.')
        if not 3 <= len(value) <= 20:
            raise serializers.ValidationError('Username must be between 3 and 20 characters long.')

        # if Account.objects.filter(username=value).exists():
        #     raise serializers.ValidationError('Username already exists.')

        return value


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(max_length=68, write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Account
        fields = ('username', 'password', 'tokens')

    def get_tokens(self, obj):  # get_{field_name}
        username = obj.get('username')
        tokens = Account.objects.get(username=username).tokens
        return tokens

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed({
                'message': 'Account disabled'
            })

        return attrs


class MyAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'username', 'role', 'get_role_display', 'first_name', 'last_name', 'bio', 'created_date')


class AccountUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'username', 'first_name', 'last_name', 'avatar', 'bio', 'role', 'get_role_display')
        extra_kwargs = {
            'role': {'read_only': True},
            'avatar': {'required': False},
            'username': {'required': False},
        }
