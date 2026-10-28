from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wishes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="wishlist",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="wish_lists",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
