from rest_framework.serializers import ModelSerializer

from apps.users.models import UserModel

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'first_name', 'last_name', "address", "postal_code", "phone_number"]