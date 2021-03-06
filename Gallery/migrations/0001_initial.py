# Generated by Django 2.1 on 2018-09-23 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImageName', models.CharField(max_length=250)),
                ('DisplayName', models.CharField(max_length=350)),
                ('ImageUrl', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ImgInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Discription', models.CharField(max_length=5000)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gallery.Gallery')),
            ],
        ),
    ]
