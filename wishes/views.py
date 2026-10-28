from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import WishItemForm, WishListForm
from .models import WishItem, WishList


def home(request):
    lists = WishList.objects.prefetch_related("items").order_by("-created_at")
    return render(request, "wishes/home.html", {"lists": lists})


def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("wishes:home")
    return render(request, "registration/signup.html", {"form": form})


@login_required
def create_list(request):
    form = WishListForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        wish_list = form.save(commit=False)
        wish_list.owner = request.user
        wish_list.save()
        return redirect("wishes:list_detail", pk=wish_list.pk)
    return render(request, "wishes/list_form.html", {"form": form})


def list_detail(request, pk):
    wish_list = get_object_or_404(WishList.objects.prefetch_related("items"), pk=pk)
    can_manage = request.user.is_authenticated and wish_list.owner_id == request.user.id
    return render(
        request,
        "wishes/list_detail.html",
        {"wish_list": wish_list, "form": WishItemForm(), "can_manage": can_manage},
    )


@login_required
@require_POST
def add_item(request, pk):
    wish_list = get_object_or_404(WishList, pk=pk, owner=request.user)
    form = WishItemForm(request.POST)
    if form.is_valid():
        item = form.save(commit=False)
        item.wish_list = wish_list
        item.save()
        if request.headers.get("HX-Request"):
            return render(request, "wishes/partials/item.html", {"item": item})
    return redirect("wishes:list_detail", pk=pk)


@require_POST
def claim_item(request, pk):
    item = get_object_or_404(WishItem, pk=pk)
    item.claimed = not item.claimed
    item.claimed_by = request.POST.get("claimed_by", "").strip() if item.claimed else ""
    item.save(update_fields=["claimed", "claimed_by"])
    if request.headers.get("HX-Request"):
        return render(request, "wishes/partials/item.html", {"item": item})
    return redirect("wishes:list_detail", pk=item.wish_list_id)
