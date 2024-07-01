from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lms_app", "0003_count_lessons"),
    ]

    operations = [
        migrations.DeleteModel(
            name="count_lessons",
        ),
    ]