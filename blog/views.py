from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Job
from .forms import PostForm, JobForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

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

def job_new(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.author = request.user
            job.published_date = timezone.now()
            job.save()
            return redirect('blog.views.post_detail', pk=job.pk)
    else:
        form = JobForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def job_list(request):
    jobs = Job.objects.order_by('created_date')
    return render(request, 'blog/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'blog/job_detail.html', {'job': job})