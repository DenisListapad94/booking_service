from django.contrib.auth.models import User
from  django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from booking_app.models import HotelsComment
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

from .paginations import CustomPagination
from .serializers import UserModelSerializer


class SomeDataViewClass(APIView):
    def get(self, request, format=None):
        data = {"message": "Hello, world!"}
        return Response(data)


#
# class UserApiView(APIView):
#
#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         users = User.objects.get(pk=pk)
#         serializer = UserSerializer(users, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def post(self, request, format=None):
#         user = UserSerializer(data=request.data)
#
#         if user.is_valid():
#             user.save()
#             return Response(user.data, status=status.HTTP_201_CREATED)
#         return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         user = User.objects.get(pk=pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class UserListApiView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    # pagination_class = [CustomPagination]
    filterset_fields = ['is_superuser', 'is_staff','first_name']
    search_fields = ['first_name', 'last_name', "username"]
    ordering_fields = ['username', 'first_name',"last_name"]
    #
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

#
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    #
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)



#
# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})

# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world!"})
