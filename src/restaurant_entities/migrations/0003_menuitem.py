# Generated by Django 3.0 on 2020-11-01 17:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_entities', '0002_auto_20201024_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Unique global identifier', unique=True, verbose_name='Global ID')),
                ('picture', models.ImageField(upload_to='images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
