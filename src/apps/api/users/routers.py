from rest_framework import routers

from apps.api.users.viewsets import UserViewSet


router = routers.DefaultRouter()


router.register(r'users', UserViewSet)
urlpatterns = router.urls