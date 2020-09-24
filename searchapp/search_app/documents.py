from django.contrib.auth import get_user_model
from elasticsearch_dsl.query import MultiMatch
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import ZztempCodinghw2Model


@registry.register_document
class ModelDocument(Document):
    class Index:
        name = 'temps'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = ZztempCodinghw2Model
        fields = [
            'text1',
            'text2'
        ]
