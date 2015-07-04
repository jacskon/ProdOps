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
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(
        default="MM/DD/YYYY")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

#
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.first_name

class Roster(models.Model):
    emp_id = models.ForeignKey(Employee)
    team = models.CharField(max_length=30)
    day = models.CharField(max_length=30)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.first_name









# """jobName1    jobParams1    jobTarget1    jobTargetType1    jobCredentials1    jobDescription1
# jobName2    jobParams2    jobTarget2    jobTargetType2    jobCredentials2    jobDescription2
# """