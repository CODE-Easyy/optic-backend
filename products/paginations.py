from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ProductPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data, maxi, mini):
        return Response({
            'count': self.page.paginator.count,
            'min': mini,
            'max': maxi,
            'results': data
        })