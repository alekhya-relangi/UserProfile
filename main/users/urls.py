from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r"dashboard/", views.dashboard, name="dashboard"),
    url(r'accounts/',include("django.contrib.auth.urls")),
    url(r"register/",views.register,name='register'),
    url(r"delete/",views.delete_user, name='delete'),
]