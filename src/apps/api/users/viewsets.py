from rest_framework.viewsets import ModelViewSet

from apps.users.models import UserModel
from apps.api.users.serializers import UserModelSerializer


class UserViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer