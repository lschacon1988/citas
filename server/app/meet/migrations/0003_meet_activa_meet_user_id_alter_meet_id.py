# Generated by Django 4.1.7 on 2023-03-21 14:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('meet', '0002_alter_meet_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='activa',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='meet',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AlterField(
            model_name='meet',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
