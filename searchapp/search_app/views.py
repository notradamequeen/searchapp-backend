from elasticsearch_dsl.query import MultiMatch
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from search_app.documents import AutocompleteDocument
from search_app.serializers import AutocompleteSerializer


# Create your views here.
class SearchAppApiView(APIView):
    def get(self, request, format=None):
        search_text = request.query_params.get('search').strip()
        q = MultiMatch(
            query=search_text,
            fields=['text1', 'text2'],
            fuzziness=2)
        qs = AutocompleteDocument.search().query(q)
        try:
            response = qs.execute()
            hits = response.hits.hits
            serializer = AutocompleteSerializer(hits)
            result = serializer.data
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=str(e))
        return Response(data=result)
