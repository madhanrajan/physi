from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Topic


@registry.register_document
class TopicDocument(Document):

    document = fields.TextField(attr="get_document_text")

    class Index:
        name = 'topics'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Topic

        fields = [
            'title',
        ]
