from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseForbidden
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from .forms import HotelForm
from .models import Person, User, Hobby, Hotel


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
    context = {
        "comments": comments
    }
    return render(
        request=request,
        template_name="user_comment.html",
        context=context
    )


def persons_view(request):
    context = {
        # "persons": Person.objects.prefetch_related("hotel_comments").prefetch_related("hobbies")
        "persons": Person.objects.filter(sex="f").order_by("-age", "created_at").prefetch_related(
            "hotel_comments").prefetch_related("hobbies")[:20]
    }
    return render(
        request=request,
        template_name="persons.html",
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

        hotel_form = HotelForm(request.POST)
        if hotel_form.is_valid():
            Hotel.objects.create(
                name=request.POST["name"],
                stars=request.POST["stars"]
            )
            return HttpResponseRedirect(reverse("persons"))
        else:

            hotel_form = HotelForm()
            return  HttpResponseForbidden(request)


    else:
        hotel_form = HotelForm()
    context = {
        "form": hotel_form
    }
    return render(
        request=request,
        template_name="hotel_add_form.html",
        context=context
    )
