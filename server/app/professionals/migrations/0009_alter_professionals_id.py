# Generated by Django 4.1.7 on 2023-08-03 17:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0008_remove_professionals_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionals',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
