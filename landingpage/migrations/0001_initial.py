# Generated by Django 2.0.1 on 2018-02-16 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=200, verbose_name='Business Name')),
                ('about', models.TextField(verbose_name='About')),
                ('main_img', models.ImageField(upload_to='media/upload/landingpage', verbose_name='Center piece image')),
            ],
        ),
    ]