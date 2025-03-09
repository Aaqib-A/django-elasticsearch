from django.urls import re_path

from book.views.es_book_view import ESBookView

urlpatterns = [
    re_path(r'^search$', ESBookView.as_view()),
]
