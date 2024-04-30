from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


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
