from django.urls import path
from . import views

app_name = "wishes"
urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("lists/new/", views.create_list, name="create_list"),
    path("lists/<int:pk>/", views.list_detail, name="list_detail"),
    path("lists/<int:pk>/items/new/", views.add_item, name="add_item"),
    path("items/<int:pk>/claim/", views.claim_item, name="claim_item"),
]
