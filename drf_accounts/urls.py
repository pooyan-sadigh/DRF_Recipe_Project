from django.urls import path

from .views import CreateAccountView, CreateTokenView, ManageAccountView

app_name = 'account'

urlpatterns = [
    path('create/', CreateAccountView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('me/', ManageAccountView.as_view(), name='me'),
]
