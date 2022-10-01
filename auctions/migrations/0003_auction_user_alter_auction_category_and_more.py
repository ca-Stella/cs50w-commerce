# Generated by Django 4.1 on 2022-09-30 04:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0002_auction_bids_comments"),
    ]

    operations = [
        migrations.AddField(
            model_name="auction",
            name="user",
            field=models.ForeignKey(
                default=9,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="auction",
            name="category",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="auction",
            name="url",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]
