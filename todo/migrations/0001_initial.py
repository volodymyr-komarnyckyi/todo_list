# Generated by Django 4.2.3 on 2023-07-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                (
                    "deadline_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True
                    )
                ),
                ("is_done", models.BooleanField(default=False)),
                (
                    "tags",
                    models.ManyToManyField(
                        related_name="tasks",
                        to="todo.tag")
                ),
            ],
            options={
                "ordering": ["created_datetime"],
            },
        ),
    ]
