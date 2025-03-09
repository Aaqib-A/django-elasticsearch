# REST Essentials
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ValidationError

# Custom Defined Imports
from book.models import Book
from book.documents import BookDocument
from book.serializers import BookModelSerializer


class ESBookView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            query = data['query']

            book_document = BookDocument.search().query("match", title=query).to_queryset()
            book_ser = BookModelSerializer(book_document, many=True).data

            resp = Response(book_ser, status=status.HTTP_200_OK)
            return resp

        except Exception as e:
            print(e)
            resp = Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return resp
