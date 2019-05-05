"""Users app serializers"""

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from .models import Patient, Psychologist


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {
                'style': {'input_type': 'password'},
                'write_only': True,
                'min_length': 5
            }
        }

    def create(self, validated_data):
        """Creates a new user with encrypted password and returns it"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for a patient"""

    class Meta:
        model = Patient
        exclude = ('user',)

    def create(self, validated_data):
        """Creates a new patient instance"""
        user = self.context.get('request').user
        return Patient.objects.create(**validated_data, user=user)


class PsychologistSerializer(serializers.ModelSerializer):
    """Serializer for a patient"""

    class Meta:
        model = Psychologist
        exclude = ('user',)

    def create(self, validated_data):
        """Creates a new psychologist instance"""
        user = self.context.get('request').user
        return Psychologist.objects.create(**validated_data, user=user)

