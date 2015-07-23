from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def approved_comments(self):
        return self.comments.filter(approved=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Job(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    parameters = models.TextField()
    target = models.CharField(max_length=200)
    target_type = models.CharField(max_length=200)
    credentials = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Event(models.Model):
    WEEKLY = 'WEEKLY'
    FORTNIGHTLY = 'FORTNIGHTLY'
    MONTHLY = 'MONTHLY'
    DAILY = 'DAILY'
    how_often = (
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (FORTNIGHTLY, 'Fortnightly'),
        (MONTHLY, 'Monthly'),
    )
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    Days = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )
    NA = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    startweek = (
        (NA, 'N/A'),
        (ONE, 'First'),
        (TWO, 'Second'),
        (THREE, 'Third'),
        (FOUR, 'Fourth'),
    )
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now, null=True)
    frequency = models.CharField(max_length=20, choices=how_often)
    day = models.IntegerField(choices=Days)
    start_week = models.IntegerField(choices=startweek)

    def __str__(self):
        return self.name

class Team(models.Model):
    team_name = models.CharField(max_length=30)

    def __str__(self):
        return self.team_name

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.first_name

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=True)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text

