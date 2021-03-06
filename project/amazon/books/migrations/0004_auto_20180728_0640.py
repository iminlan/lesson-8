# Generated by Django 2.0.7 on 2018-07-28 06:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180721_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='lastname',
            field=models.CharField(default='', max_length=100, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
    ]
