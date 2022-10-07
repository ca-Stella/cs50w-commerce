# Generated by Django 4.1 on 2022-10-04 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0011_comment_delete_comments_auction_closed_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="comment", new_name="text",
        ),
        migrations.AddField(
            model_name="comment",
            name="listing",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="auctions.auction",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]