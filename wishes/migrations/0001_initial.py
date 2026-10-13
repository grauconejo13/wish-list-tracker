from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="WishList",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("recipient_name", models.CharField(max_length=100)),
                ("occasion", models.CharField(blank=True, max_length=80)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="WishItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=160)),
                ("url", models.URLField(blank=True)),
                ("price", models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ("notes", models.TextField(blank=True)),
                ("claimed", models.BooleanField(default=False)),
                ("claimed_by", models.CharField(blank=True, max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("wish_list", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="items", to="wishes.wishlist")),
            ],
        ),
    ]
