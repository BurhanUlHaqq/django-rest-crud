from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'page_size'  # Allows client to set page size
    max_page_size = 100  # Maximum page size allowed

    def get_paginated_response(self, data):
        return Response({
            'draw': int(self.request.query_params.get('draw', 1)),  # Draw is required for DataTables to sync requests
            'recordsTotal': self.page.paginator.count,  # Total records without filtering
            'recordsFiltered': self.page.paginator.count,  # Total records after filtering, same here if no filter
            'data': data,  # The actual paginated data
        })