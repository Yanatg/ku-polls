# Generated by Django 4.2.2 on 2023-09-06 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="end_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="date ended"
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="pub_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="date published"
            ),
        ),
    ]
