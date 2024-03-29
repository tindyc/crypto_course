# Generated by Django 3.2.6 on 2023-03-17 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('subject', models.CharField(max_length=50)),
                ('your_message', models.TextField(max_length=1000)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Form Submissions',
            },
        ),
    ]
