import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lms_app", "0002_alter_lesson_video_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="count_lessons",
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
                (
                    "count_course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="count_lessons",
                        to="lms_app.course",
                    ),
                ),
                (
                    "count_lessons",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="count_lessons",
                        to="lms_app.lesson",
                    ),
                ),
            ],
        ),
    ]