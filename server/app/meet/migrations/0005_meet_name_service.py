# Generated by Django 4.1.7 on 2023-05-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0004_rename_professional_id_meet_professional_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='name_service',
            field=models.CharField(default='Tradicional', max_length=50),
        ),
    ]
