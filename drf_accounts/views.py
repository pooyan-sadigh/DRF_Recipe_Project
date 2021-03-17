from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import AccountSerializer, AuthTokenSerializer


class CreateAccountView(generics.CreateAPIView):
    """creates a new account"""

    serializer_class = AccountSerializer


class CreateTokenView(ObtainAuthToken):
    """creates a new auth token for the account"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageAccountView(generics.RetrieveUpdateAPIView):
    """manage the authenticated account"""

    serializer_class = AccountSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """retrieve and return authenticated account"""
        return self.request.user
