from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    SomeDataViewClass,
    UserListApiView,
    UserDetail,
)

urlpatterns = [
    # path('some_url_example', hello_world),
    path('some_url_example', SomeDataViewClass.as_view()),
    path('users', UserListApiView.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)