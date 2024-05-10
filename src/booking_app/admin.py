from django.contrib import admin

from .models import (
    Person, Profile,
    Hotel, HotelsComment,
    BookInfo, Hobby, User,
    HotelOwner,PersonComment
)

admin.site.register(Person)
admin.site.register(Profile)
admin.site.register(Hotel)
admin.site.register(HotelsComment)
admin.site.register(Hobby)
admin.site.register(BookInfo)
admin.site.register(HotelOwner)
admin.site.register(PersonComment)
admin.site.register(User)

