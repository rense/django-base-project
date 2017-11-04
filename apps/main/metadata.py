from rest_framework.metadata import BaseMetadata, SimpleMetadata


class NoMetadata(BaseMetadata):
    """ Stop DRF from leaking data in OPTIONS
    """
    def determine_metadata(self, request, view):
        return None


class MinimalMetadata(SimpleMetadata):
    """
    """
    def determine_metadata(self, request, view):
        serializer = view.get_serializer()
        fields = self.get_serializer_info(serializer)
        return {
            'name': view.get_view_name(),
            'fields': fields
        }
