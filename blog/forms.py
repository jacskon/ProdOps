from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from blog.models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('name', 'parameters', 'target', 'target_type', 'credentials', 'description',)

class EventForm(forms.ModelForm):

    class Meta:
        model = Event

        fields = ('name', 'description', 'day', 'frequency', 'start_week',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class PbiForm(forms.ModelForm):

    class Meta:
        model = Pbi
        fields = ('number', 'title', 'description', 'severity', 'status', 'assignee', 'estimated_finish', 'state')

class OperationsForm(forms.ModelForm):

    class Meta:
        model = Pbi
        fields = ('title', 'description', 'severity', 'status', 'assignee', 'estimated_finish', 'progress_bar', 'state')

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('user',)

class UpdateForm(forms.ModelForm):

    class Meta:
        model = Update
        fields = ('text', 'update_type')

# """jobName1    jobParams1    jobTarget1    jobTargetType1    jobCredentials1    jobDescription1
# jobName2    jobParams2    jobTarget2    jobTargetType2    jobCredentials2    jobDescription2
# """