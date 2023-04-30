from django.urls import path
from . import views

urlpatterns = [
	path("", views.Login.as_view(), name="login"),
	path("home", views.Index.as_view(), name="index"),
	path("about", views.About.as_view(), name="about"),
	path("signup", views.Signup.as_view(), name="signup"),
	path("chat", views.Chat.as_view(), name="chat"),
	path("my_account", views.AccountView.as_view(), name="my_account"),
]
