#import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .models import Image
from rest_framework import generics, filters
from .serializers import ImageSerializer
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination


class ImageList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    #filter_fields = ['title']
    search_fields = ['title']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class ImageCreate(generics.ListCreateAPIView):
#     queryset = Image.objects.all(),
#     serializer_class = ImageSerializer
#
#
# class ImageList(APIView):
#     # queryset = Image.objects.all()
#     # serializer_class = ImageSerializer
#     def get(self, request, format=None):
#         image = Image.objects.all()
#         serializer = ImageSerializer(image, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDetail(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


# class ImageUpdate(generics.RetrieveUpdateAPIView):
#     # API endpoint that allows a customer record to be updated.
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer