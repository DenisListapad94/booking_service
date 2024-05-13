from django.contrib import admin

from .models import (
    Person, Profile,
    Hotel, HotelsComment,
    BookInfo, Hobby, User,
    HotelOwner, PersonComment
)


class BookInfoInline(admin.StackedInline):
    model = BookInfo


class HotelsCommentInline(admin.TabularInline):
    model = HotelsComment


@admin.action(description="Mark rating hotels rating 4.5 stars")
def make_five_stars(modeladmin, request, queryset):
    # import pdb;pdb.set_trace()
    queryset.update(rating=4.5)


# @admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "stars", "rating", "view_rating_stars", "owners"]
    list_display_links = ["name", "address"]
    # fields = [("name", "address"), ("stars", "rating"),"owners"]
    # exclude = ["rating"]
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "address"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["wide", "collapse"],
                "fields": [("stars", "rating"), "owners"],
            },
        ),
    ]
    list_filter = ["stars", "address"]
    readonly_fields = ["rating"]
    ordering = ["-stars", "name"]
    search_fields = ["name", "stars"]
    list_editable = ["stars"]
    list_per_page = 7
    save_on_top = True
    inlines = [
        BookInfoInline,
    ]
    actions = [
        make_five_stars,
    ]

    @admin.display(description='Звёздный Рейтинг')
    def view_rating_stars(self, obj):
        return f"{obj.stars} : {obj.rating}"


class HobbyInline(admin.TabularInline):
    model = Hobby.owners.through
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [
        HobbyInline,
    ]


admin.site.register(Person)
admin.site.register(Profile)
admin.site.register(Hotel, HotelAdmin)

admin.site.register(HotelsComment)
admin.site.register(Hobby)
admin.site.register(BookInfo)
admin.site.register(HotelOwner)
admin.site.register(PersonComment)
admin.site.register(User, UserAdmin)
