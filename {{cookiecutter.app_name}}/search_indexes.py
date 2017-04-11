from haystack import indexes

from .models import {{ cookiecutter.model_name }}


class {{ cookiecutter.model_name }}Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return {{ cookiecutter.model_name }}
