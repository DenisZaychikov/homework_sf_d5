from django.db import models


class Friend(models.Model):
    full_name = models.TextField(default=None)
    age = models.SmallIntegerField()

    def __str__(self):
        return self.full_name


class PublishingHouse(models.Model):
    pb_house_name = models.TextField()

    def __str__(self):
        return self.pb_house_name


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    pb_house = models.ForeignKey(PublishingHouse, null=True, on_delete=models.CASCADE)
    friend_name = models.ForeignKey(Friend, null=True, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
