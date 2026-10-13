from django import forms
from .models import WishItem, WishList


class WishListForm(forms.ModelForm):
    class Meta:
        model = WishList
        fields = ["title", "recipient_name", "occasion"]


class WishItemForm(forms.ModelForm):
    class Meta:
        model = WishItem
        fields = ["name", "url", "price", "notes"]
