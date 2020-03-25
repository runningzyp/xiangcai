# Generated by Django 3.0.3 on 2020-02-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("blog", "0010_article_body_html")]

    operations = [
        migrations.AddField(
            model_name="article",
            name="body_toc",
            field=models.TextField(blank=True, null=True, verbose_name="文章目录"),
        ),
        migrations.AlterField(
            model_name="article",
            name="body",
            field=models.TextField(verbose_name="文章"),
        ),
        migrations.AlterField(
            model_name="article",
            name="body_html",
            field=models.TextField(blank=True, null=True, verbose_name="转码文章"),
        ),
    ]