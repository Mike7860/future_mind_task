from django.urls import include, path
from .views import ImageList, ImageDetail


urlpatterns = [
    path('', ImageList.as_view(), name='create-image'),
   # path('', ImageList.as_view(), name='list-images'),
    path('<int:pk>/', ImageDetail.as_view(), name='retrieve-image')
]