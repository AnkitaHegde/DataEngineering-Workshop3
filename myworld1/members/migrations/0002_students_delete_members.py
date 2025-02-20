# Generated by Django 4.2 on 2023-04-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('roll_number', models.IntegerField()),
                ('mobile', models.CharField(max_length=10)),
                ('branch', models.CharField(choices=[('BA', 'BA'), ('B.COM', 'B.COM'), ('MBA', 'MBA'), ('CA', 'CA')], max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Members',
        ),
    ]
