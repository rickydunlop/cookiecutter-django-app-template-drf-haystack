from rest_framework import viewsets

from .models import {{ cookiecutter.model_name }}
from .serializers import {{ cookiecutter.model_name }}Serializer


class {{ cookiecutter.model_name }}ViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing {{ app_name }}.
    """
    queryset = {{ cookiecutter.model_name }}.objects.all()
    serializer_class = {{ cookiecutter.model_name }}Serializer
