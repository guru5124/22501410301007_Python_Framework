from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('demo/', views.demo, name="demo"),
    path('curdate/', views.cur_date, name="curdate"),
    path('converter/<int:n>/', views.path_converter, name="converter_int"),
    path('converter/<str:n>/', views.path_converter, name="converter_str"),
    path('converter/<slug:n>/', views.path_converter, name="converter_slug"),

    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('post/', views.post_details, name="post"),
    path('base/', views.base, name="base"),
    path('contact/', views.contact, name="contact"),
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('send-email/', views.send_test_email, name="send_email"),

    path('post-form/', views.post_view, name="post_form"),

    # ================= CATEGORY =================
    path('category/', views.category_view, name="category"),
    path('category/edit/<int:id>/', views.edit_category, name='edit_category'),
    path('category/delete/<int:id>/', views.delete_category, name='delete_category'),

    # ================= POSTS =================
    path('posts/', views.show_post, name='show_post'),
    path('create/', views.create_post, name='create_post'),
    path('update/<int:id>/', views.update_post, name='update_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
]