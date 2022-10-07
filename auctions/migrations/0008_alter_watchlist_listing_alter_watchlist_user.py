# Generated by Django 4.1 on 2022-10-02 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0007_watchlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="watchlist",
            name="listing",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="watcher",
                to="auctions.auction",
            ),
        ),
        migrations.AlterField(
            model_name="watchlist",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="watched",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]