# Generated by Django 4.0.8 on 2022-11-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_blogpost_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Tag Name', max_length=30, verbose_name='Tag')),
                ('foreground', models.CharField(default='#fff', help_text='Enter Foreground Decoration', max_length=100, verbose_name='Foreground')),
                ('background', models.CharField(default='#000', help_text='Enter Background Decoration', max_length=100, verbose_name='Background')),
            ],
        ),
    ]