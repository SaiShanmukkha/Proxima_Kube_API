# Generated by Django 4.0.8 on 2022-12-03 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='static/images/todo.png', upload_to='api/images/'),
        ),
    ]
