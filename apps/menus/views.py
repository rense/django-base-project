from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.menus.models import MenuItem
from apps.menus.serializers import MenuItemSerializer


class MenuViewSet(ReadOnlyModelViewSet):
    model = MenuItem
    lookup_field = 'pk'
    permission_classes = (AllowAny,)

    serializer_class = MenuItemSerializer

    def get_queryset(self):
        return self.model.published.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(parent__isnull=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
