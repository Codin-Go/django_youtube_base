# Generated by Django 4.0.5 on 2022-07-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catube', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]