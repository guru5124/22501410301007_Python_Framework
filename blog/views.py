from django.shortcuts import render, HttpResponse
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

from .models import ContactUs

# BASIC VIEWS


def demo(request):
    return HttpResponse("Welcome to Django Framework")


def cur_date(request):
    time = datetime.now()
    return HttpResponse(f"Current Date & Time: {time}")


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

# CONTACT FORM

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

# EMAIL

def send_test_email(request):
    send_mail(
        subject='Test Email',
        message='Hello! This is a test email from Django.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['user@example.com'],
        fail_silently=False,
    )
    return HttpResponse("Email sent (check console).")

# LOGIN

def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, 'login.html', {'msg': "Login Success", 'form': form})

    return render(request, 'login.html', {'form': form})

# REGISTRATION


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

# POST FORM 

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

# CATEGORY FORM 

def category_view(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "category.html", {
                "form": CategoryForm(),
                "msg": "Category Saved Successfully"
            })

    return render(request, "category.html", {"form": form})

# is_valid()
def register(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            return render(request, "register.html", {"msg": "Registration Successful"})
        else:
            print(form.errors)   

    return render(request, "register.html", {"form": form})

# Program 17
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# program 21
#CREATE (Insert Data)
from django.shortcuts import render, redirect
from .models import Post

def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        content = request.POST.get('content')
        author = request.POST.get('author')

        Post.objects.create(
            title=title,
            slug=slug,
            content=content,
            author=author
        )
        return redirect('show_post')

    return render(request, 'create_post.html')

#READ (Display Data)
def show_post(request):
    posts = Post.objects.all()
    return render(request, 'show_post.html', {'posts': posts})
#UPDATE (Edit Data)
def update_post(request, id):
    post = Post.objects.get(id=id)

    if request.method == "POST":
        post.title = request.POST.get('title')
        post.slug = request.POST.get('slug')
        post.content = request.POST.get('content')
        post.author = request.POST.get('author')
        post.save()
        return redirect('show_post')

    return render(request, 'update_post.html', {'post': post})
#DELETE (Remove Data)
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('show_post')