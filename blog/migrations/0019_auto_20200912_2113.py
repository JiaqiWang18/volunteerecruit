# Generated by Django 3.1 on 2020-09-13 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_post_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='address',
            field=models.CharField(help_text='Location of this activity', max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_time',
            field=models.DateTimeField(help_text='Event time', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, help_text='Attach a flyer (optional)', upload_to='post_thumbnails', verbose_name='Flyer'),
        ),
    ]
