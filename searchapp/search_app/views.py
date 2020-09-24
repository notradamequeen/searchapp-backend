from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render
from elasticsearch_dsl.query import MultiMatch
from rest_framework.response import Response
from rest_framework.views import APIView
from search_app.documents import ModelDocument


# Create your views here.
class SearchAppApiView(APIView):
    def get(self, request, format=None):
        search_text = request.query_params.get('search').strip()
        q = MultiMatch(query=search_text, fields=['text1', 'text2'], fuzziness=2)
        qs = ModelDocument.search().query(q)
        response = qs.execute()
        response = sorted(response.hits.hits, key=lambda t: t._source.text1)
        response = sorted(response, key=lambda h: h['_score'], reverse=True)
        result = [dict(score=r._score, text1=r._source.text1, text2=r._source.text2) for r in response]
        return Response(data=result)
