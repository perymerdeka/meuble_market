from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication

from apps.users.models import UserModel
from apps.api.users.serializers import UserModelSerializer


class UserViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = []
