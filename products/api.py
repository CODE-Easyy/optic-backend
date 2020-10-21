from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)
import json

from .models import (
    Product,
    SubCategory
)
from events.models import Event

from .serializers import (
    ProductsListSerializer,
    SubCategoriesSerializer,
    ProductDetailSerializer,
)

from .map_filters import getQS
from .paginations import ProductPagination

class ProductsCartList(ListAPIView):
    queryset = Product.objects.all()
    def get(self, request, *args, **kwargs):
        ids = self.request.query_params.get('ids', None)
        if ids:
            ids = list(map(int, str(ids).strip().split(',')))
            qs = Product.objects.filter(id__in=ids)
            qs = qs.order_by('id')
            serializer = ProductsListSerializer(qs, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"error": "ID's not listed!!!"}, status.HTTP_404_NOT_FOUND)





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

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        data = {
            "id": obj.pk,
            "title": obj.title,
            "description": obj.description,
            "price": obj.price,
            "img_1": obj.img_1.absolute_url if obj.img_1 else None,
            "img_2": obj.img_2.absolute_url if obj.img_2 else None,
            "img_3": obj.img_3.absolute_url if obj.img_3 else None,
            "cat": obj.cat,
            "is_new": obj.is_new,
            "is_leader": obj.is_leader,
            "is_discount": obj.is_discount,
            "discount": obj.discount,
            "sex": obj.sex,
            "subcat": obj.subcat.id,
            "brand": obj.brand.value if obj.brand else None,
            "material": obj.material.value if obj.material else None,
            "radius": obj.radius.value if obj.radius else None,
            "opt_power": obj.opt_power.value if obj.opt_power else None,
            "volume": obj.volume.value if obj.volume else None
        }
        return Response(data)

class ProductsList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer

    def get(self, request, *args, **kwargs):
        qs = Product.objects.all()
        cat = self.request.query_params.get('cat', None)
        subcat = self.request.query_params.get('subcat', None)
        bool = self.request.query_params.get('bool', None)
        event = self.request.query_params.get('event', None)

        #FILTERS
        brands = self.request.query_params.get('brand', None)
        materials = self.request.query_params.get('material', None)
        radiuses = self.request.query_params.get('radius', None)
        sexes = self.request.query_params.get('sex', None)
        max_price = self.request.query_params.get('max', None)
        min_price = self.request.query_params.get('min', None)
        opt_powers = self.request.query_params.get('opt_power', None)
        volumes = self.request.query_params.get('volume', None)


        if event:
            e = Event.objects.get(id=int(event))
            serializer = ProductsListSerializer(e.products, many=True, context={'request': request})
            return Response(serializer.data, status.HTTP_200_OK)


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

            if brands:
                brand = brands.strip().split(',')
                qs = qs.filter(brand__value__in=brand)
            if sexes:
                sex = sexes.strip().split(',')
                qs = qs.filter(sex__in=sex)
            if materials:
                material = materials.strip().split(',')
                qs = qs.filter(material__value__in=material)
            if opt_powers:
                optical_power = opt_powers.strip().split(',')
                qs = qs.filter(opt_power__value__in=optical_power)
            if radiuses:
                radius = radiuses.strip().split(',')
                qs = qs.filter(radius__value__in=radius)
            if volumes:
                volume = volumes.strip().split(',')
                qs = qs.filter(volume__value__in=volume)
            print(min_price, max_price)
            if min_price:
                qs = qs.filter(price__gte=min_price)
            if max_price:
                qs = qs.filter(price__lte=max_price)

        paginator = ProductPagination()
        page = paginator.paginate_queryset(qs, self.request)
        serializer = ProductsListSerializer(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data, mini=min([i.price for i in Product.objects.all()]), maxi=max([i.price for i in Product.objects.all()]))












class VolumesList(ListAPIView):
    ''' List of volumes  '''

    queryset = Product.objects.all()
    def get(self, request, *args, **kwargs):
        qs = Product.objects.all().values('volume').distinct()
        cat = self.request.query_params.get('cat', None)
        subcat = self.request.query_params.get('subcat', None)
        if cat:
            qs = qs.filter(cat=cat).values('volume').distinct()
        if subcat:
            qs = qs.filter(subcat=subcat).values('volume').distinct()

        qs = list(filter(None, map(getQS, qs)))
        seen = set()
        new_qs = []
        for d in qs:
            t = tuple(d.items())
            if t not in seen:
                seen.add(t)
                new_qs.append(d)
        return Response(new_qs, status=status.HTTP_200_OK)


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
        seen = set()
        new_qs = []
        for d in qs:
            t = tuple(d.items())
            if t not in seen:
                seen.add(t)
                new_qs.append(d)
        return Response(new_qs, status=status.HTTP_200_OK)

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
        seen = set()
        new_qs = []
        for d in qs:
            t = tuple(d.items())
            if t not in seen:
                seen.add(t)
                new_qs.append(d)
        return Response(new_qs, status=status.HTTP_200_OK)

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
        seen = set()
        new_qs = []
        for d in qs:
            t = tuple(d.items())
            if t not in seen:
                seen.add(t)
                new_qs.append(d)
        return Response(new_qs, status=status.HTTP_200_OK)

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
        seen = set()
        new_qs = []
        for d in qs:
            t = tuple(d.items())
            if t not in seen:
                seen.add(t)
                new_qs.append(d)
        return Response(new_qs, status=status.HTTP_200_OK)


