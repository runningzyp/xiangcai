# Generated by Django 2.2.5 on 2019-11-25 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("blog", "0005_auto_20191125_1337")]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField()),
                ("create_time", models.DateTimeField(auto_now=True)),
                ("modify_time", models.DateTimeField(auto_now_add=True)),
                (
                    "article",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="comments",
                        related_query_name="comments",
                        to="blog.Article",
                        verbose_name="评论主体",
                    ),
                ),
            ],
            options={"verbose_name": "评论", "verbose_name_plural": "评论"},
        )
    ]
