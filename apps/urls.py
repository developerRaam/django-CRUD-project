from django.urls import path,include
from .import views

# admin.site.site_header = "Ecommerce Lucknow Admin"
# admin.site.site_title = "Ecommerce Admin Portal"
# admin.site.index_title = "Welcome to Ecommerce Portal"

urlpatterns = [
    path("",views.Home,name="home"),
    path("login/",views.Login, name="login"),
    path("register/", views.Register, name="register"),
    path("report/", views.Report, name="report"),
    path("logout/",views.Logout, name="logout"),
]