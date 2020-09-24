from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
    TrigramSimilarity,
    SearchVectorField
)
from django.db import models
from django.db.models import Q

# Create your models here.
class ZztempCodinghw2ModelManager(models.Manager):
    def search(self, text):
        search_vectors = (
            SearchVector('text1', weight='A') +
            SearchVector('text2', weight='B')
        )
        search_query = SearchQuery(text)
        search_rank = SearchRank(search_vectors, search_query)
        trigram_similarity = (TrigramSimilarity('text1', text) +
                              TrigramSimilarity('text2', text)) / 2
        return self.get_queryset().annotate(
            search=search_vectors,
            trigram_similarity=trigram_similarity,
            rank=search_rank + trigram_similarity
        ).filter(
            Q(search=search_query) |
            Q(rank__gte=0.27)
        ).order_by('-rank', 'text1')


class ZztempCodinghw2Model(models.Model):
    id = models.BigAutoField(primary_key=True)
    text1 = models.TextField()
    text2 = models.TextField()

    objects = ZztempCodinghw2ModelManager()

    class Meta:
        db_table = 'zztemp_codinghw2'
        app_label = 'doc_search'
