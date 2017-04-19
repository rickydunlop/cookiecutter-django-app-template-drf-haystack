from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializerMixin

from .models import {{ cookiecutter.model_name }}
from .search_indexes import {{ cookiecutter.model_name }}Index


class {{ cookiecutter.model_name }}Serializer(serializers.ModelSerializer):

    class Meta:
        model = {{ cookiecutter.model_name }}
        fields = '__all__'


class {{ cookiecutter.model_name }}SearchSerializer(HaystackSerializerMixin, {{ cookiecutter.model_name }}Serializer):
    groupby_key = serializers.SerializerMethodField()

    def get_groupby_key(self, obj):
        return obj._meta.verbose_name_plural.title()

    class Meta({{ cookiecutter.model_name }}Serializer.Meta):
        index_classes = [{{ cookiecutter.model_name }}Index]
