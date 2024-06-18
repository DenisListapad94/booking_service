import base64
from .tasks import create_photo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
import requests
from django.core.files.base import ContentFile

from .forms import HotelModelForm
from .models import Person, User, Hobby, HotelsComment, Hotel


# function base view
def some_view(request, some_int, some_str):
    return HttpResponse(f"<h1>hello django app some int: {some_int} some str: {some_str}</h1>")


# def some_new_view(request, year):
#     return HttpResponse(f"<h1>regular expression view  some year {year} </h1>")

class MyView(View):
    def get(self, request, year):
        return HttpResponse(f"<h1>regular expression view  some year {year} </h1>")


# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def get_info_user(self):
#         return f"name :{self.name} age: {self.age}"


# def some_template_view(request):
#     # context = {
#     #     "some_arg": "hello world",
#     #     "some_list": [4, 2, 6, 1, 15, 16, 21],
#     #     "user": User("Jhon", 45)
#     # }
#
#     return render(
#         request=request,
#         template_name="base.html",
#         # context=context
#     )

def home_view(request):
    return render(
        request=request,
        template_name="home.html",
    )


comments = [
    {
        "number": 1,
        "user_id": 1,
        "name": "John",
        "comment": "some John comment"
    },
    {
        "number": 2,
        "user_id": 2,
        "name": "Ann",
        "comment": "some Ann comment"
    },
    {
        "number": 3,
        "user_id": 3,
        "name": "Peter",
        "comment": "some Peter comment"
    },
]


def user_comment_view(request):
    comments = HotelsComment.objects.all()

    paginator = Paginator(comments, 10)  # Show 20 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj
    }
    return render(
        request=request,
        template_name="user_comment.html",
        context=context
    )


class UserCommentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ["booking_app.view_hotelscomment"]
    login_url = "/admin/login/"
    template_name = "user_comment.html"
    model = HotelsComment
    # queryset = HotelsComment.objects.all()
    context_object_name = "comments"
    paginate_by = 20
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["comments"] = HotelsComment.objects.all()[:10]#comments
    #     return context


# @cache_page(timeout=60)
@permission_required("booking_app.view_person", login_url="/admin/login/")
@login_required(login_url="/admin/login/")
def persons_view(request):
    context = {
        # "persons": Person.objects.prefetch_related("hotel_comments").prefetch_related("hobbies")
        "persons": Person.objects.filter(sex="f").order_by("-age", "created_at").prefetch_related(
            "hotel_comments").prefetch_related("hobbies")[:20]
    }
    # from time import sleep
    # sleep(10)
    return render(
        request=request,
        template_name="persons.html",
        context=context
    )

def show_hotels(request):
    context = {
        "hotels":Hotel.objects.all()
    }
    from config.celery import debug_task
    # debug_task.delay(15)

    return render(
        request=request,
        template_name="hotels.html",
        context=context
    )

def hotels_view_delete(request):
    with transaction.atomic():
        user = User.objects.get(pk=1)
        # import pdb;pdb.set_trace()
        user.first_name = "Ann"
        user.save()
        hobby = Hobby.objects.get(pk=22)

        # print(user)
    return HttpResponse(f"<h1></h1>")


def hotels_form(request):
    if request.method == "POST":

        form = HotelModelForm(request.POST,request.FILES)
        if form.is_valid():
            if 'photo' in form.files:
                form.save()
            else:
                create_photo.delay(form.cleaned_data)

            return HttpResponseRedirect(reverse("persons"))
    else:
        form = HotelModelForm()
    context = {
        "form": form
    }
    return render(
        request=request,
        template_name="hotel_add_form.html",
        context=context
    )


# class HotelFormView(CreateView):
#     template_name = "hotel_add_form.html"
#     form_class = HotelModelForm
#     reverse_lazy = "persons"
