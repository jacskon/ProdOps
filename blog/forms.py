from django import forms

from .models import Post, Job

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('name', 'parameters', 'target', 'target_type', 'credentials', 'description',)
# """jobName1    jobParams1    jobTarget1    jobTargetType1    jobCredentials1    jobDescription1
# jobName2    jobParams2    jobTarget2    jobTargetType2    jobCredentials2    jobDescription2
# """