from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

from .models import (
    Product,
    SubCategory
)

from .serializers import (
    ProductsListSerializer,
    SubCategoriesSerializer,
    ProductDetailSerializer,

)

from .map_filters import getQS
from .paginations import ProductPagination


class SubCategoriesList(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoriesSerializer

    def get(self, request, *args, **kwargs):
        qs = SubCategory.objects.all()
        cat = self.request.query_params.get('cat', None)

        if cat:
            qs = qs.filter(cat=cat)

        serializer = SubCategoriesSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class ProductsList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer

    def get(self, request, *args, **kwargs):
        qs = Product.objects.all()
        cat = self.request.query_params.get('cat', None)
        subcat = self.request.query_params.get('subcat', None)
        bool = self.request.query_params.get('bool', None)

        if bool:
            if bool == 'new':
                qs = qs.filter(is_new=True)
            elif bool == 'leader':
                qs = qs.filter(is_leader=True)
            elif bool == 'discount':
                qs = qs.filter(is_discount=True)

            serializer = ProductsListSerializer(qs, many=True, context={'request': request})
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            if cat:
                qs = qs.filter(cat=cat)
            if subcat:
                qs = qs.filter(subcat=subcat)

        paginator = ProductPagination()
        page = paginator.paginate_queryset(qs, self.request)
        serializer = ProductsListSerializer(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)












class VolumesList(ListAPIView):
    ''' List of volumes  '''

    queryset = Product.objects.all()
    def get(self, request, *args, **kwargs):
        qs = Product.objects.all().values('volume').distinct();
        cat = self.request.query_params.get('cat', None)
        subcat = self.request.query_params.get('subcat', None)
        if cat:
            qs = qs.filter(cat=cat).values('volume').distinct()
        if subcat:
            qs = qs.filter(subcat=subcat).values('volume').distinct()

        qs = list(filter(None, map(getQS, qs)))
        return Response(qs, status=status.HTTP_200_OK)


class MaterialsList(ListAPIView):
    ''' List of materials  '''
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        qs = Product.objects.all().values('material').distinct();
        cat = self.request.query_params.get('cat', None)
        subcat = self.request.query_params.get('subcat', None)
        if cat:
            qs = qs.filter(cat=cat).values('material').distinct()
        if subcat:
            qs = qs.filter(subcat=subcat).values('material').distinct()

        qs = list(filter(None, map(getQS, qs)))
        return Response(qs, status=status.HTTP_200_OK)

class BrandsList(ListAPIView):
    ''' List of brands  '''
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        qs = Product.objects.all().values('brand').distinct();
        cat = self.request.query_params.get('cat', None)
        subcat = self.request.query_params.get('subcat', None)
        if cat:
            qs = qs.filter(cat=cat).values('brand').distinct()
        if subcat:
            qs = qs.filter(subcat=subcat).values('brand').distinct()
        qs = list(filter(None, map(getQS, qs)))
        return Response(qs, status=status.HTTP_200_OK)

class RadiusesList(ListAPIView):
    ''' List of radiuses  '''
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        qs = Product.objects.all().values('radius').distinct();
        cat = self.request.query_params.get('cat', None)
        subcat = self.request.query_params.get('subcat', None)
        if cat:
            qs = qs.filter(cat=cat).values('radius').distinct()
        if subcat:
            qs = qs.filter(subcat=subcat).values('radius').distinct()
        qs = list(filter(None, map(getQS, qs)))
        return Response(qs, status=status.HTTP_200_OK)

class OpticalPowersList(ListAPIView):
    ''' List of brands  '''
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        qs = Product.objects.all().values('opt_power').distinct();
        cat = self.request.query_params.get('cat', None)
        subcat = self.request.query_params.get('subcat', None)
        if cat:
            qs = qs.filter(cat=cat).values('opt_power').distinct()
        if subcat:
            qs = qs.filter(subcat=subcat).values('opt_power').distinct()
        qs = list(filter(None, map(getQS, qs)))
        return Response(qs, status=status.HTTP_200_OK)


