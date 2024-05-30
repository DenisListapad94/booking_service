from django.urls import path,include,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .views import (
    SomeDataViewClass,
    UserListApiView,
    UserDetail,
)

urlpatterns = [
    # path('some_url_example', hello_world),
    path("jwt/create",TokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify", TokenVerifyView.as_view(), name="jwt-verify"),
    path('some_url_example', SomeDataViewClass.as_view()),
    path('users', UserListApiView.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)