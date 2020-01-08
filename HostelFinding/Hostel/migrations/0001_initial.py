# Generated by Django 3.0.1 on 2020-01-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Location', models.CharField(max_length=50)),
                ('Picture', models.ImageField(upload_to='')),
                ('Description', models.TextField()),
            ],
        ),
    ]