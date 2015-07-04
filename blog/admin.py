from django.contrib import admin
from .models import Post, Job, Event, Employee, Roster


admin.site.register(Post)
admin.site.register(Job)
admin.site.register(Event)
admin.site.register(Employee)
admin.site.register(Roster)