from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings

from .forms import (
    LoginForm,
    ContactUsForm,
    RegistrationForm,
    PostForm,
    CategoryForm
)

from .models import ContactUs, Category, Post


# ================= BASIC VIEWS =================

def demo(request):
    return HttpResponse("Welcome to Django Framework")


def cur_date(request):
    return HttpResponse(f"Current Date & Time: {datetime.now()}")


def path_converter(request, n):
    return HttpResponse(f"User Entered: {n}")


def home(request):
    return render(request, "home.html", {'msg': "Welcome Harshil"})


def about(request):
    data = {
        "Blog_author": "Harshil Jadav",
        "post_title": "Django Template Filters",
        "date": datetime.now()
    }
    return render(request, "about.html", data)


def post_details(request):
    post_title = [
        {'title': "Python Framework", 'recent': True},
        {'title': "Django Tutorial", 'recent': False},
        {'title': "Flask Tutorial", 'recent': True},
        {'title': ".NET Framework", 'recent': False},
    ]
    return render(request, "post_detail.html", {'Title': post_title})


def base(request):
    return render(request, "base.html")


# ================= CONTACT =================

def contact(request):
    form = ContactUsForm()

    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contact.html", {
                "form": ContactUsForm(),
                "msg": "Saved Successfully"
            })

    return render(request, "contact.html", {"form": form})


# ================= EMAIL =================

def send_test_email(request):
    send_mail(
        subject='Test Email',
        message='Hello! This is a test email from Django.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['user@example.com'],
        fail_silently=False,
    )
    return HttpResponse("Email sent (check console).")


# ================= LOGIN =================

def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, 'login.html', {
                'msg': "Login Success",
                'form': form
            })

    return render(request, 'login.html', {'form': form})


# ================= REGISTRATION =================

def register(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return render(request, "register.html", {
                "msg": "Registration Successful",
                "form": RegistrationForm()
            })

    return render(request, "register.html", {"form": form})


# ================= POST FORM =================

def post_view(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "post.html", {
                "form": PostForm(),
                "msg": "Post Saved Successfully"
            })

    return render(request, "post.html", {"form": form})


# ================= CATEGORY =================

def category_view(request):
    form = CategoryForm()
    result = ""

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            result = "Category Saved Successfully"
            form = CategoryForm()

    data = Category.objects.all()

    return render(request, "category.html", {
        "form": form,
        "data": data,
        "result": result
    })


# EDIT CATEGORY
def edit_category(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')

    form = CategoryForm(instance=category)
    data = Category.objects.all()

    return render(request, "category.html", {
        "form": form,
        "data": data
    })


# DELETE CATEGORY
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category')


# ================= POST CRUD =================

# CREATE
def create_post(request):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST.get('title'),
            slug=request.POST.get('slug'),
            content=request.POST.get('content'),
            author=request.POST.get('author')
        )
        return redirect('show_post')

    return render(request, 'create_post.html')


# READ
def show_post(request):
    posts = Post.objects.all()
    return render(request, 'show_post.html', {'posts': posts})


# UPDATE
def update_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.title = request.POST.get('title')
        post.slug = request.POST.get('slug')
        post.content = request.POST.get('content')
        post.author = request.POST.get('author')
        post.save()
        return redirect('show_post')

    return render(request, 'update_post.html', {'post': post})


# DELETE
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('show_post')