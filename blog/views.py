from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import calendar, datetime


@login_required
def index(request):
    team = request.user.groups.all()
    return render(request, 'index.html', {'team': team})

@login_required
def post_list(request):
    pbi_task_list = Pbi.objects.all().filter(type='PBI').order_by('-modified_date')
    operations_task_list = Pbi.objects.all().filter(type='operations').order_by('-modified_date')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'pbi_task_list': pbi_task_list,
                                                   'operations_task_list': operations_task_list})

@login_required
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

@login_required
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

@login_required
def job_list(request):
    jobs = Job.objects.order_by('created_date')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
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

@login_required
def calendar_view(request):
    # pdb.set_trace()
    team = request.user.groups.all()
    events = Event.objects.filter(team=str(team))
    today = datetime.datetime.now()
    month = today.month
    month_name = today.strftime("%B")
    cals = (calendar.monthcalendar(2015, month))
    return render(request, 'calendar/calendar_list.html', {'cals': cals, 'events': events, 'month_name':  month_name,
                                                           'today': today, 'team': team})

@login_required
def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.team = request.user.groups.all()
            event.save()
            return redirect('blog.views.calendar_view')
    else:
        form = EventForm()
    return render(request, 'calendar/event_create.html', {'form': form})

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

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'calendar/event_detail.html', {'event': event})

@login_required
def event_remove(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('blog.views.calendar_view')

@login_required
def schedule(request):
    weeks = (calendar.monthcalendar(2015, 6))
    cals = (calendar.monthcalendar(2015, 6))
    num_days = 7
    return render(request, 'roster/roster.html', {'cals': cals, 'num_days': num_days})

@login_required
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

@login_required
def pbi_view(request):
    pbi = Pbi.objects.all()
    task_list = Task.objects.all()
    medium_sum = pbi.filter(severity='Medium').count()
    low_sum = pbi.filter(severity='Low').count()
    high_sum = pbi.filter(severity='High').count()
    critical_sum = pbi.filter(severity='Critical').count()
    assigned_sum = pbi.filter(status='Assigned').count()
    under_investigation_sum = pbi.filter(status='Under investigation').count()
    in_progress_sum = pbi.filter(status='In Progress').count()
    low_status_sum = pbi.filter(status='Low').count()
    pending_sum = pbi.filter(status='Pending').count()
    return render(request, 'pbi/pbi_list.html', {'pbi': pbi, 'medium_sum': medium_sum, 'low_sum': low_sum,
                                                 'high_sum': high_sum, 'critical_sum': critical_sum,
                                                 'assigned_sum': assigned_sum, 'under_investigation_sum': under_investigation_sum,
                                                 'in_progress_sum': in_progress_sum, 'low_status_sum': low_status_sum,
                                                 'pending_sum': pending_sum, 'task_list': task_list})


@login_required
def operations_view(request):
    operations_tasks = Pbi.objects.all().filter(type='operations')
    task_list = Task.objects.all()
    medium_sum = operations_tasks.filter(severity='Medium').count()
    low_sum = operations_tasks.filter(severity='Low').count()
    high_sum = operations_tasks.filter(severity='High').count()
    critical_sum = operations_tasks.filter(severity='Critical').count()
    assigned_sum = operations_tasks.filter(status='Assigned').count()
    under_investigation_sum = operations_tasks.filter(status='Under investigation').count()
    in_progress_sum = operations_tasks.filter(status='In Progress').count()
    low_status_sum = operations_tasks.filter(status='Low').count()
    pending_sum = operations_tasks.filter(status='Pending').count()
    return render(request, 'pbi/operations_list.html', {'operations_tasks': operations_tasks, 'medium_sum': medium_sum, 'low_sum': low_sum,
                                                 'high_sum': high_sum, 'critical_sum': critical_sum,
                                                 'assigned_sum': assigned_sum, 'under_investigation_sum': under_investigation_sum,
                                                 'in_progress_sum': in_progress_sum, 'low_status_sum': low_status_sum,
                                                 'pending_sum': pending_sum, 'task_list': task_list})


@login_required
def pbi_new(request, task_type):
    if request.method == "POST":
        form = PbiForm(request.POST)
        if form.is_valid():
            pbi = form.save(commit=False)
            pbi.type = task_type
            pbi.save()
            return redirect('blog.views.'+task_type+'_view')
    else:
        if task_type == 'pbi':
            form = PbiForm
        elif task_type == 'operations':
            form = OperationsForm
    return render(request, 'pbi/pbi_create.html', {'form': form, 'task_type': task_type})

@login_required
def pbi_edit(request, pk):
    pbi = get_object_or_404(Pbi, pk=pk)
    if request.method == "POST":
        form = PbiForm(request.POST, instance=pbi)
        if form.is_valid():
            pbi = form.save(commit=False)
            current_timezone = timezone.localtime(timezone.now())
            update_time = '{:%d-%m-%Y:%H:%M:%S}'.format(current_timezone)
            pbi.updates = '[' + update_time + ']' + '   -    ' + pbi.next_action + '    -    ' \
                          + (str(request.user)).capitalize() + '\n' + pbi.updates
            pbi.modified_date = timezone.now()
            pbi.save()
            return redirect('blog.views.pbi_view')
    else:
        form = PbiForm(instance=pbi)
    return render(request, 'pbi/pbi_edit.html', {'form': form})

@login_required
def pbi_detail(request, pk):
    pbi = get_object_or_404(Pbi, pk=pk)
    return render(request, 'pbi/pbi_detail.html', {'pbi': pbi})

@login_required
def pbi_remove(request, pk):
    pbi = get_object_or_404(Pbi, pk=pk)
    pbi.delete()
    return redirect('blog.views.pbi_view')

@login_required
def pbi_chart(request):
    return render(request, 'pbi/chart.html')

@login_required
def task_edit(request, pk):
    task_type = request.GET.get('type', '')
    print(task_type)
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.modified_date = timezone.now()
            task.save()
            return redirect('blog.views.pbi_view')
    else:
        if task_type == 'operations':
            form = TaskForm(instance=task)
        elif task_type == 'pbi':
            form = OperationsForm(instance=task)
    return render(request, 'task/task_edit.html', {'form': form, 'task_type': task_type})
