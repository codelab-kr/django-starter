# Generated by Django 5.0.4 on 2024-05-06 09:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Act",
            fields=[
                ("title", models.CharField(max_length=500)),
                ("url", models.URLField(max_length=500, null=True)),
                ("image", models.URLField(max_length=500)),
                ("body", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
