from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Job, Event, Comment
from .forms import PostForm, JobForm, EventForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import pdb
import calendar


@login_required
def index(request):
    return render(request, 'index.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def job_new(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.author = request.user
            job.published_date = timezone.now()
            job.save()
            return redirect('blog.views.job_detail', pk=job.pk)
    else:
        form = JobForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def job_list(request):
    jobs = Job.objects.order_by('created_date')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')


def calendar_view(request):
    # pdb.set_trace()
    events = Event.objects.all()
    cals = (calendar.monthcalendar(2015, 7))
    return render(request, 'calendar/calendar_list.html', {'cals': cals, 'events': events})

def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('blog.views.calendar_view')
    else:
        form = EventForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.published_date = timezone.now()
            event.save()
            return redirect('blog.views.calendar_view')
    else:
        form = EventForm(instance=event)
    return render(request, 'calendar/event_edit.html', {'form': form})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'calendar/event_detail.html', {'event': event})

def event_remove(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('blog.views.calendar_view')

def schedule(request):
    weeks = (calendar.monthcalendar(2015, 6))
    cals = (calendar.monthcalendar(2015, 6))
    num_days = 7
    return render(request, 'roster/roster.html', {'cals': cals, 'num_days': num_days})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)