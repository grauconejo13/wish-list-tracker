from django.db import models


class WishList(models.Model):
    title = models.CharField(max_length=120)
    recipient_name = models.CharField(max_length=100)
    occasion = models.CharField(max_length=80, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} — {self.recipient_name}"


class WishItem(models.Model):
    wish_list = models.ForeignKey(WishList, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=160)
    url = models.URLField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    claimed = models.BooleanField(default=False)
    claimed_by = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
