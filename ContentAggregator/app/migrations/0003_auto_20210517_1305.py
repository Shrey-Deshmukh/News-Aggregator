# Generated by Django 3.1.5 on 2021-05-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210517_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='CovidContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='hiringcontent',
            name='description',
        ),
        migrations.RemoveField(
            model_name='progcontent',
            name='description',
        ),
        migrations.RemoveField(
            model_name='pycontent',
            name='description',
        ),
        migrations.AddField(
            model_name='hiringcontent',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='progcontent',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pycontent',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
    ]
