# Generated by Django 5.0.3 on 2024-03-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=900)),
                ('Age', models.IntegerField()),
                ('Address', models.CharField(max_length=900)),
                ('Gender', models.CharField(max_length=900)),
                ('DOB', models.DateField()),
                ('Photo', models.ImageField(upload_to='images')),
            ],
        ),
    ]
