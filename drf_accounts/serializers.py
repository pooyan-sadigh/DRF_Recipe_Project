from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _


class AccountSerializer(serializers.ModelSerializer):
    """serializer for account object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'username')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """creates a new account with hashed password"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """updates the account, sets password correctly and return it"""
        password = validated_data.pop('password', None)
        account = super().update(instance, validated_data)
        if password:
            account.set_password(password)
            account.save()

        return account


class AuthTokenSerializer(serializers.Serializer):
    """serializer for account authentication using token"""

    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """validate and authenticate the account"""
        email = attrs.get('email')
        password = attrs.get('password')

        account = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not account:
            msg = _('authentication failed')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = account
        return attrs
