from django.db import models


class User(models.Model):
    SEX_PERSON = {
        "m": "male",
        "f": "female",
    }
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_PERSON,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    class Meta:
        indexes = [
            models.Index(fields=["first_name"], name="first_name_idx"),
            models.Index(fields=["age"], name="age_idx"),
            models.Index(fields=["sex"], name="sex_idx"),
        ]

    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class Person(User):
    guest_rating = models.IntegerField(null=True)


class HotelOwner(User):
    owner_exp_status = models.IntegerField(null=True)


class Hobby(models.Model):
    name = models.CharField(max_length=30, null=True)
    detail = models.CharField(max_length=200, null=True)
    owners = models.ManyToManyField(
        to="User",
        related_name="hobbies"
    )

    def __str__(self):
        return f" {self.name}"


class Profile(models.Model):
    photo = models.ImageField(null=True, blank=True)
    id_card_number = models.IntegerField(null=True)
    serial = models.CharField(null=True, max_length=30)
    persons = models.OneToOneField(
        to="User",
        on_delete=models.CASCADE,
        null=True,
        related_name="profile"
    )


class BookInfo(models.Model):
    detail = models.CharField(max_length=200, null=True)
    book_time = models.DateTimeField(auto_now_add=True)
    persons = models.ForeignKey(
        to="Person",
        on_delete=models.SET_NULL,
        null=True,
        related_name='booking_info'

    )
    hotels = models.ForeignKey(
        to="Hotel",
        on_delete=models.SET_NULL,
        null=True,
        related_name='booking_info'
    )


class Hotel(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    stars = models.IntegerField(null=True)
    rating = models.FloatField(null=True)
    owners = models.ForeignKey(
        to="HotelOwner",
        on_delete=models.SET_NULL,
        null=True,
        related_name="hotels",
    )

    def __str__(self):
        return f" {self.name}"


class Comment(models.Model):
    comment = models.CharField(max_length=200, null=True)
    comment_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


class HotelsComment(Comment):
    hotel_rating = models.PositiveIntegerField(null=True)
    hotels = models.ForeignKey(
        to="Hotel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="hotel_comments"
    )
    persons = models.ForeignKey(
        to="Person",
        on_delete=models.SET_NULL,
        null=True,
        related_name="hotel_comments"
    )

    def __str__(self):
        return f" {self.comment}"


class PersonComment(Comment):
    person_rating = models.PositiveIntegerField(null=True)
    hotels = models.ForeignKey(
        to="Hotel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="person_comments"
    )
    persons = models.ForeignKey(
        to="Person",
        on_delete=models.SET_NULL,
        null=True,
        related_name="person_comments"
    )

    def __str__(self):
        return f" {self.comment}"
