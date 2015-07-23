from django import forms
from blog.models import Post, Job, Event, Comment

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

# """jobName1    jobParams1    jobTarget1    jobTargetType1    jobCredentials1    jobDescription1
# jobName2    jobParams2    jobTarget2    jobTargetType2    jobCredentials2    jobDescription2
# """