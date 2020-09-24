from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import AutocompleteModel


@registry.register_document
class AutocompleteDocument(Document):
    class Index:
        name = 'temps'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = AutocompleteModel
        fields = [
            'text1',
            'text2'
        ]
